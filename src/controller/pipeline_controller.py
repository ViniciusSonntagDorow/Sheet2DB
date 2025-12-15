import pandas as pd
from typing import Optional

from model.csv_reader import CSVReader
from model.excel_reader import ExcelReader
from model.pandera_validator import PanderaValidator
from model.postgres_loader import PostgresLoader

from view.web_ui import WebUI


class PipelineController:
    """
    Controller responsible for orchestrating the data pipeline.
    Handles user interactions, validates data, and coordinates between View and Model.
    """

    def __init__(self, view: WebUI):
        self.view = view

        # Model components
        self.csv_reader = CSVReader()
        self.excel_reader = ExcelReader()
        self.validator = PanderaValidator()
        self.loader = PostgresLoader()

    def run(self):
        """Main application loop"""
        self.view.show_header()

        home, insert, upload, view, manage = self.view.show_navigation()

        with home:
            self._home_flow()

        with insert:
            self._insert_flow()

        with upload:
            self._upload_flow()

        with view:
            self._view_flow()

        with manage:
            self._manage_flow()

    def _home_flow(self):
        """Display home page"""
        self.view.show_home()

    def _insert_flow(self):
        """Handle manual data insertion"""
        # Get data from view
        expense_data = self.view.get_insert_form_data()

        if expense_data and expense_data.get("submitted"):
            # Process the data (controller's job)
            try:
                # Create DataFrame from form data
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

                # Validate data
                validated_df = self.validator.validate_data(df)

                # Load to database
                self.loader.load_data(validated_df)

                # Show success message
                self.view.show_success("Expense inserted successfully! 💾")

            except Exception as e:
                # Show error message
                self.view.show_error(f"Error inserting expense: {str(e)}")

    def _upload_flow(self):
        """Handle file upload and batch processing"""
        # Get file type selection
        file_type = self.view.get_upload_option()

        if file_type:
            # Get uploaded file
            uploaded_file = self.view.get_uploaded_file(file_type)

            if uploaded_file:
                try:
                    # Read data based on file type (Model's job)
                    df = self._read_file(uploaded_file, file_type)

                    # Show preview to user
                    self.view.show_dataframe_preview(df)

                    # Validate data
                    if self.view.ask_confirmation("Validate and load data?"):
                        validated_df = self.validator.validate(df)

                        # Load to database
                        self.loader.load_data(validated_df)

                        self.view.show_success(
                            f"Successfully loaded {len(validated_df)} records! 💾"
                        )

                except Exception as e:
                    self.view.show_error(f"Error processing file: {str(e)}")

    def _read_file(self, file, file_type: str) -> pd.DataFrame:
        """Read file based on type (Model interaction)"""
        if file_type.lower() == "csv":
            return self.csv_reader.read_data(file)
        elif file_type.lower() in ["excel", "xlsx"]:
            return self.excel_reader.read_data(file)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    def _view_flow(self):
        """Display data visualization"""
        try:
            # Fetch data from database (Model's job)
            df = self._fetch_data_from_db()

            if df is not None and not df.empty:
                # Pass data to view for display
                self.view.show_data_view(df)
            else:
                self.view.show_info("No data available to display.")

        except Exception as e:
            self.view.show_error(f"Error loading data: {str(e)}")

    def _fetch_data_from_db(self) -> Optional[pd.DataFrame]:
        """Fetch data from database (placeholder - implement based on your needs)"""
        # TODO: Implement data fetching from PostgreSQL
        # For now, return None to indicate under development
        return None

    def _manage_flow(self):
        """Handle data management operations"""
        self.view.show_manage()
