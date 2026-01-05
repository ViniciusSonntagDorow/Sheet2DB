import pandas as pd
import pandera as pa
from enum import Enum

from model.pandera_validator import PanderaValidator
from model.postgres_loader import PostgresLoader
from model.postgres_reader import PostgresReader

from view.web_ui import WebUI


class PipelineController:
    def __init__(self, view: WebUI):
        self.view = view

        self.postgres_reader = PostgresReader()
        self.validator = PanderaValidator()
        self.loader = PostgresLoader()

    def run(self):
        self.view.show_header()

        tabs = self.view.show_navigation()

        with tabs.home:
            self._home_flow()

        with tabs.insert:
            self._insert_flow()

        with tabs.view:
            self._view_flow()

        with tabs.manage:
            self._manage_flow()

    def _home_flow(self):
        self.view.show_home()

    def _insert_flow(self):
        expense_data = self.view.get_insert_form()

        if expense_data.get("submitted"):
            try:
                df = pd.DataFrame(
                    [
                        {
                            "expense_date": expense_data["date"],
                            "description": expense_data["description"],
                            "category": expense_data["category"],
                            "amount": expense_data["amount"],
                        }
                    ]
                )

                validated_df = self.validator.validate_data(df)

                validated_df["user"] = "user"
                validated_df["created_at"] = pd.Timestamp.now()

                self.loader.load_data(validated_df)

                self.view.show_success("Expense inserted successfully!")

            except pa.errors.SchemaErrors as schema_error:
                self.view.show_error(
                    f"❌ Data validation failed: Found {len(schema_error.failure_cases)} validation errors"
                )
                self.view.show_dataframe_preview(schema_error.failure_cases)

            except Exception as e:
                self.view.show_error(f"Error inserting expense: {str(e)}")

    def _view_flow(self):
        try:
            df = self.postgres_reader.read_data("SELECT * FROM expenses")

            if df is not None and not df.empty:
                self.view.show_data_view(df)
            else:
                self.view.show_info("No data available to display.")

        except Exception as e:
            self.view.show_error(f"Error loading data: {str(e)}")

    def _manage_flow(self):
        self.view.show_manage()
