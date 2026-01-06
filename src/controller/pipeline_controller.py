import pandas as pd
import pandera as pa
import streamlit as st

from model.pandera_validator import PanderaValidator
from model.postgres_loader import PostgresLoader
from model.postgres_reader import PostgresReader
from model.postgres_deleter import PostgresDeleter

from view.web_ui import WebUI
from utils.config import config


class PipelineController:
    def __init__(self, view: WebUI):
        self.view = view

        self.postgres_reader = PostgresReader()
        self.validator = PanderaValidator()
        self.loader = PostgresLoader()
        self.deleter = PostgresDeleter()

    def run(self):
        self.view.show_header()

        tabs = self.view.show_navigation()

        with tabs.home:
            self._home_flow()

        with tabs.insert:
            self._insert_flow()

        with tabs.dashboard:
            self._dashboard_flow()

        with tabs.delete:
            self._delete_flow()

    def _home_flow(self):
        self.view.show_home()

    def _insert_flow(self):
        insert_data = self.view.get_insert_form()

        if insert_data.get("submitted"):
            try:
                df = pd.DataFrame(
                    [
                        {
                            "expense_date": insert_data["date"],
                            "description": insert_data["description"],
                            "category": insert_data["category"],
                            "amount": insert_data["amount"],
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

    def _dashboard_flow(self):
        try:
            df = self.postgres_reader.read_data(
                "SELECT expense_date, description, category, amount FROM expenses"
            )

            if df is not None and not df.empty:
                self.view.show_dashboard(df)
            else:
                self.view.show_info("No data available to display.")

        except Exception as e:
            self.view.show_error(f"Error loading data: {str(e)}")

    def _delete_flow(self):
        df = self.postgres_reader.read_data("SELECT * FROM expenses")

        delete_data = self.view.get_delete_form(df)

        if delete_data.get("submitted"):
            try:
                selected_ids = delete_data.get("selected_ids", [])

                if selected_ids:
                    deleted_count = self.deleter.delete_by_ids(
                        config.POSTGRES_TABLE, selected_ids
                    )

                    if deleted_count > 0:
                        self.view.show_success(
                            f"Successfully deleted {deleted_count} record(s)!"
                        )
                        st.rerun()  # Refresh the page to show updated data
                    else:
                        self.view.show_warning("No records were deleted.")

            except Exception as e:
                self.view.show_error(f"Error managing data: {str(e)}")
