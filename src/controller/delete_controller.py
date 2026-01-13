from view.streamlit_view import StreamlitView
from model.postgres_reader import PostgresReader
from model.postgres_deleter import PostgresDeleter


class DeleteController:
    def __init__(
        self,
        view: StreamlitView,
        reader: PostgresReader,
        deleter: PostgresDeleter,
        table_name: str,
    ):
        self._view = view
        self._reader = reader
        self._deleter = deleter
        self._table_name = table_name

    def execute(self) -> None:
        df = self._reader.read_data("SELECT * FROM expenses")

        delete_data = self._view.get_delete_form(df)

        if delete_data.get("submitted"):
            try:
                selected_ids = delete_data.get("selected_ids", [])

                if selected_ids:
                    deleted_count = self._deleter.delete_by_ids(
                        self._table_name, selected_ids
                    )

                    if deleted_count > 0:
                        self._view.show_success(
                            f"Successfully deleted {deleted_count} record(s)!"
                        )
                        self._view.refresh()
                    else:
                        self._view.show_warning("No records were deleted.")

            except Exception as e:
                self._view.show_error(f"Error managing data: {str(e)}")
