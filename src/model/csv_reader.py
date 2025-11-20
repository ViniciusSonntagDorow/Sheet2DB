import pandas as pd

from model.reader import Reader


class CSVReader(Reader):
    def __init__(
        self,
        sep: str = ",",
        encoding: str = "utf-8",
        engine: str = "pyarrow",
        dtype_backend: str = "pyarrow",
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
