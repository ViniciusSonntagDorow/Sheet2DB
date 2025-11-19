from abc import ABC, abstractmethod
import pandas as pd


class IRead(ABC):
    @abstractmethod
    def read_data(self, file: str) -> pd.DataFrame:
        pass


class IValidate(ABC):
    @abstractmethod
    def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


class ITransform(ABC):
    @abstractmethod
    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


class ILoad(ABC):
    @abstractmethod
    def load_data(self, df: pd.DataFrame) -> None:
        pass
