import pandas as pd


class PostgresReader:
    def __init__(
        self,
        connection_string: str,
        dtype_backend: str = "pyarrow",
    ):
        self._connection_string = connection_string
        self._dtype_backend = dtype_backend

    def read_data(self, query: str) -> pd.DataFrame:
        return pd.read_sql(
            query,
            con=self._connection_string,
            dtype_backend=self._dtype_backend,
        )
