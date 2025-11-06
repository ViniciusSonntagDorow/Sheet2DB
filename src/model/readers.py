from interfaces import IRead
import pandas as pd


class CSVReader(IRead):
    def __init__(self):
        super().__init__()

    def extract_data(self, file: str) -> pd.DataFrame:
        """Extract the CSV file into a DataFrame.

        Args:
            file (str): Path to the CSV file.

        Returns:
            pd.DataFrame: The data as a DataFrame.
        """
        import pandas as pd

        return pd.read_csv(file)
