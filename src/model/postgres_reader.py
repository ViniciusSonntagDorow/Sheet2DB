import pandas as pd

from model.reader import Reader
from utils.config import config


class PostgresReader(Reader):
    def __init__(
        self,
        dtype_backend: str = config.DTYPE_BACKEND,
    ):
        self.__dtype_backend = dtype_backend

    def read_data(self, query: str) -> pd.DataFrame:
        return pd.read_sql(
            query,
            con=config.get_connection_string(),
            dtype_backend=self.__dtype_backend,
        )
