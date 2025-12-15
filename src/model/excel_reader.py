import pandas as pd

from model.reader import Reader
from utils.config import config


class ExcelReader(Reader):
    def __init__(
        self,
        engine: str = config.EXCEL_ENGINE,
        dtype_backend: str = config.DTYPE_BACKEND,
    ):
        self.__engine = engine
        self.__dtype_backend = dtype_backend

    def read_data(self, file: str) -> pd.DataFrame:
        xls = pd.ExcelFile(file, engine=self.__engine)

        if len(xls.sheet_names) != 1:
            raise ValueError(
                f"Error: Your Excel file must have only 1 sheet, {len(xls.sheet_names)} were submitted."
            )

        return pd.read_excel(
            file,
            sheet_name=0,
            engine=self.__engine,
            dtype_backend=self.__dtype_backend,
        )
