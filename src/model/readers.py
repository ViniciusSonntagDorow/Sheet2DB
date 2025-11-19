import pandas as pd

from model.interfaces import IRead


class CSVReader(IRead):
    def __init__(
        self,
        sep: str = ",",
        encoding: str = "utf-8",
        engine: str = "pyarrow",
        dtype_backend: str = "pyarrow",
    ):
        self.engine = engine
        self.dtype_backend = dtype_backend
        self.sep = sep
        self.encoding = encoding

    def read_data(self, file: str) -> pd.DataFrame:
        return pd.read_csv(
            file,
            sep=self.sep,
            encoding=self.encoding,
            engine=self.engine,
            dtype_backend=self.dtype_backend,
        )


class ExcelReader(IRead):
    def __init__(self, engine: str = "calamine", dtype_backend: str = "pyarrow"):
        self.engine = engine
        self.dtype_backend = dtype_backend

    def read_data(self, file: str) -> pd.DataFrame:
        xls = pd.ExcelFile(file, engine=self.engine)

        if len(xls.sheet_names) != 1:
            raise ValueError(
                f"Error: Your Excel file must have only 1 sheet, {len(xls.sheet_names)} were submitted."
            )

        return pd.read_excel(
            file,
            sheet_name=0,
            engine=self.engine,
            dtype_backend=self.dtype_backend,
        )
