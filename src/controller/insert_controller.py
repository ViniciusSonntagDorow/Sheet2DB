import pandas as pd
import pandera as pa

from view.streamlit_view import StreamlitView
from model.pandera_validator import PanderaValidator
from model.postgres_loader import PostgresLoader


class InsertController:
    def __init__(
        self,
        view: StreamlitView,
        validator: PanderaValidator,
        loader: PostgresLoader,
        table_name: str,
    ):
        self._view = view
        self._validator = validator
        self._loader = loader
        self._table_name = table_name

    def execute(self) -> None:
        insert_data = self._view.get_insert_form()

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

                validated_df = self._validator.validate_data(df)

                validated_df["user"] = "user"
                validated_df["created_at"] = pd.Timestamp.now()

                self._loader.load_data(validated_df, self._table_name)

                self._view.show_success("Expense inserted successfully!")

            except pa.errors.SchemaErrors as schema_error:
                self._view.show_error(
                    f"❌ Data validation failed: Found {len(schema_error.failure_cases)} validation errors"
                )
                self._view.show_dataframe_preview(schema_error.failure_cases)

            except Exception as e:
                self._view.show_error(f"Error inserting expense: {str(e)}")
