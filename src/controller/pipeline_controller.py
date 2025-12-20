import pandas as pd
import pandera as pa
from enum import Enum

from model.csv_reader import CSVReader
from model.excel_reader import ExcelReader
from model.pandera_validator import PanderaValidator
from model.postgres_loader import PostgresLoader

from view.web_ui import WebUI


class FileType(Enum):
    """Supported file types"""

    CSV = "csv"
    EXCEL = "excel"
    XLSX = "xlsx"


class PipelineController:
    def __init__(self, view: WebUI):
        self.view = view

        self.csv_reader = CSVReader()
        self.excel_reader = ExcelReader()
        self.validator = PanderaValidator()
        self.loader = PostgresLoader()

    def run(self):
        self.view.show_header()

        tabs = self.view.show_navigation()

        with tabs.home:
            self._home_flow()

        with tabs.insert:
            self._insert_flow()

        with tabs.upload:
            self._upload_flow()

        with tabs.view:
            self._view_flow()

        with tabs.manage:
            self._manage_flow()

    def _home_flow(self):
        self.view.show_home()

    def _insert_flow(self):
        expense_data = self.view.get_insert_form()

        if expense_data and expense_data.get("submitted"):
            try:
                df = pd.DataFrame(
                    [
                        {
                            "date": expense_data["date"],
                            "description": expense_data["description"],
                            "category": expense_data["category"],
                            "amount": expense_data["amount"],
                        }
                    ]
                )

                validated_df = self.validator.validate_data(df)

                # self.loader.load_data(validated_df)

                self.view.show_success("Expense inserted successfully! 💾")

                self.view.show_dataframe_preview(validated_df)

            except pa.errors.SchemaErrors as schema_error:
                self.view.show_error(
                    f"❌ Data validation failed: Found {len(schema_error.failure_cases)} validation errors"
                )
                self.view.show_dataframe_preview(schema_error.failure_cases)

            except Exception as e:
                self.view.show_error(f"Error inserting expense: {str(e)}")

    def _upload_flow(self):
        file_type = self.view.get_upload_option()

        if file_type:
            uploaded_file = self.view.get_uploaded_file(file_type)

            if uploaded_file:
                try:
                    df = self._read_file(uploaded_file, file_type)

                    validated_df = self.validator.validate_data(df)

                    self.view.show_dataframe_preview(validated_df)

                    if self.view.ask_confirmation(
                        "Do you want to load this data into the database?"
                    ):
                        # self.loader.load_data(validated_df)

                        self.view.show_success(
                            f"Successfully loaded {len(validated_df)} records! 💾"
                        )

                except pa.errors.SchemaErrors as schema_error:
                    self.view.show_error(
                        f"❌ Data validation failed: Found {len(schema_error.failure_cases)} validation errors"
                    )
                    self.view.show_dataframe_preview(schema_error.failure_cases)

                except Exception as e:
                    self.view.show_error(f"Error inserting expense: {str(e)}")

    def _read_file(self, file, file_type: str) -> pd.DataFrame:
        """Read file based on type"""
        file_type_lower = file_type.lower()

        if file_type_lower == FileType.CSV.value:
            return self.csv_reader.read_data(file)
        elif file_type_lower in [FileType.EXCEL.value, FileType.XLSX.value]:
            return self.excel_reader.read_data(file)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    def _view_flow(self):
        try:
            df = self._fetch_data_from_db()  # Criar um modulo pra isso

            if df is not None and not df.empty:
                self.view.show_data_view(df)
            else:
                self.view.show_info("No data available to display.")

        except Exception as e:
            self.view.show_error(f"Error loading data: {str(e)}")

    def _manage_flow(self):
        self.view.show_manage()
