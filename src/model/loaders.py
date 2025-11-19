import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os

from model.interfaces import ILoad


load_dotenv(find_dotenv())


class PostgresLoader(ILoad):
    def __init__(
        self,
        user: str = os.getenv("POSTGRES_USER"),
        password: str = os.getenv("POSTGRES_PASSWORD"),
        host: str = os.getenv("POSTGRES_HOST"),
        port: str = os.getenv("POSTGRES_PORT"),
        database: str = os.getenv("POSTGRES_DB"),
    ):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection_string = (
            f"postgresql://{user}:{password}@{host}:{port}/{database}"
        )

    def __str__(self):
        return f"PostgresLoader({self.user}@{self.host}:{self.port}/{self.database})"

    def load_data(self, df: pd.DataFrame) -> None:
        df.to_sql(
            "statements", con=self.connection_string, if_exists="append", index=False
        )
