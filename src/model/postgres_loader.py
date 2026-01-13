import pandas as pd


class PostgresLoader:
    def __init__(self, connection_string: str, table_name: str = "expenses"):
        self._connection_string = connection_string
        self._default_table_name = table_name

    def load_data(self, df: pd.DataFrame, table_name: str | None = None) -> None:
        target_table = table_name or self._default_table_name
        df.to_sql(
            target_table, con=self._connection_string, if_exists="append", index=False
        )
