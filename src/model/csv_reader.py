import pandas as pd

from model.reader import Reader
from utils.config import config


class CSVReader(Reader):
    def __init__(
        self,
        sep: str = config.CSV_SEPARATOR,
        encoding: str = config.CSV_ENCODING,
        engine: str = config.CSV_ENGINE,
        dtype_backend: str = config.DTYPE_BACKEND,
    ):
        self.__engine = engine
        self.__dtype_backend = dtype_backend
        self.__sep = sep
        self.__encoding = encoding

    def read_data(self, file: str) -> pd.DataFrame:
        return pd.read_csv(
            file,
            sep=self.__sep,
            encoding=self.__encoding,
            engine=self.__engine,
            dtype_backend=self.__dtype_backend,
        )
