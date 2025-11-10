import pandas as pd

from .base_classes import BaseReader


class CSVReader(BaseReader):
    """Implements reading of CSV files with customizable settings."""

    def __init__(
        self,
        sep: str = ",",
        encoding: str = "utf-8",
        engine: str = "pyarrow",
        dtype_backend: str = "pyarrow",
    ):
        """Initializes the CSV reader with specific pandas configurations.

        Args:
            sep (str, optional): The delimiter to use. Defaults to ",".
            encoding (str, optional): File encoding. Defaults to "utf-8".
            engine (str, optional): Parser engine (e.g., 'c', 'pyarrow'). Defaults to "pyarrow".
            dtype_backend (str, optional): Backend for data types. Defaults to "pyarrow".
        """
        super().__init__(engine=engine, dtype_backend=dtype_backend)

        self.sep = sep
        self.encoding = encoding

    def read_data(self, file: str) -> pd.DataFrame:
        """Reads a CSV file into a DataFrame using the instance's settings.

        Args:
            file (str): Path to the CSV file.

        Returns:
            pd.DataFrame: The data as a DataFrame.
        """

        return pd.read_csv(
            file,
            sep=self.sep,
            encoding=self.encoding,
            engine=self.engine,
            dtype_backend=self.dtype_backend,
        )


class ExcelReader(BaseReader):
    """Implements reading of Excel files, ensuring there is only one sheet."""

    def __init__(self, engine: str = "calamine", dtype_backend: str = "pyarrow"):
        """Initializes the Excel reader with specific pandas configurations.

        Args:
            engine (str, optional): Parser engine (e.g., 'calamine', 'openpyxl'). Defaults to "calamine".
            dtype_backend (str, optional): Backend for data types. Defaults to "pyarrow".
        """
        super().__init__(engine=engine, dtype_backend=dtype_backend)

    def read_data(self, file: str) -> pd.DataFrame:
        """Reads an Excel file into a DataFrame, validating the sheet count.

        Raises a ValueError if the file does not contain exactly one sheet.

        Args:
            file (str): Path to the Excel file.

        Raises:
            ValueError: If the file has 0 or more than 1 sheet.

        Returns:
            pd.DataFrame: The data from the single sheet as a DataFrame.
        """

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
