import pandas as pd

from model.loader import Loader
from utils.config import config


class PostgresLoader(Loader):
    def __init__(self, connection_string: str = config.get_connection_string()):
        self.__connection_string = connection_string

    def __str__(self):
        return f"PostgresLoader(connected to {config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB})"

    def load_data(
        self, df: pd.DataFrame, table_name: str = config.POSTGRES_TABLE
    ) -> None:
        df.to_sql(
            table_name, con=self.__connection_string, if_exists="append", index=False
        )
