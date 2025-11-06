from abc import ABC, abstractmethod
import pandas as pd


class IRead(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read_data(self, file: str) -> pd.DataFrame:
        """Extract the input file into a DataFrame.

        Args:
            file (str): Path to the input file.

        Returns:
            pd.DataFrame: The data as a DataFrame.
        """
        pass


class IValidate(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def validate_data(self, df: pd.DataFrame) -> bool:
        """Validate the DataFrame against a schema.

        Args:
            df (pd.DataFrame): The DataFrame to validate.

        Returns:
            bool: True if validation passes, False otherwise.
        """
        pass


class ITransform(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply transformations to the DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The transformed DataFrame.
        """
        pass


class ILoad(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load_data(self, df: pd.DataFrame, destination: str) -> None:
        """Load the DataFrame to the specified destination.

        Args:
            df (pd.DataFrame): The DataFrame to save.
            destination (str): The destination path or connection string.
        """
        pass
