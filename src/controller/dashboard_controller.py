import pandas as pd
from view.streamlit_view import StreamlitView
from view.components.dashboard import DashboardData
from model.postgres_reader import PostgresReader


class DashboardController:
    def __init__(self, view: StreamlitView, reader: PostgresReader):
        self._view = view
        self._reader = reader

    def _prepare_dashboard_data(self, df: pd.DataFrame) -> DashboardData:
        """Controller prepares all data - View only renders."""
        category_data = (
            df.groupby(["category"])["amount"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        date_data = (
            df.assign(expense_date=pd.to_datetime(df["expense_date"]).dt.normalize())
            .groupby(["expense_date"])["amount"]
            .sum()
            .reset_index()
            .sort_values("expense_date", ascending=True)
        )

        recent_expenses = df.sort_values("expense_date", ascending=False).head(20)

        return DashboardData(
            total_expenses=df["amount"].sum(),
            total_records=len(df),
            avg_amount=df["amount"].mean(),
            max_amount=df["amount"].max(),
            category_data=category_data,
            date_data=date_data,
            recent_expenses=recent_expenses,
        )

    def execute(self) -> None:
        try:
            df = self._reader.read_data(
                "SELECT expense_date, description, category, amount FROM expenses"
            )

            if df is not None and not df.empty:
                data = self._prepare_dashboard_data(df)
                self._view.show_dashboard(data)
            else:
                self._view.show_info("No data available to display.")

        except Exception as e:
            self._view.show_error(f"Error loading data: {str(e)}")
