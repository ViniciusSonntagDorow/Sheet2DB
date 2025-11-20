import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os

from model.loader import Loader


load_dotenv(find_dotenv())


class PostgresLoader(Loader):
    def __init__(
        self,
        user: str = os.getenv("POSTGRES_USER"),
        password: str = os.getenv("POSTGRES_PASSWORD"),
        host: str = os.getenv("POSTGRES_HOST"),
        port: str = os.getenv("POSTGRES_PORT"),
        database: str = os.getenv("POSTGRES_DB"),
    ):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.__database = database
        self.__connection_string = f"postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}"

    def __str__(self):
        return f"PostgresLoader({self.__user}@{self.__host}:{self.__port}/{self.__database})"

    def load_data(self, df: pd.DataFrame) -> None:
        df.to_sql(
            "statements", con=self.__connection_string, if_exists="append", index=False
        )
