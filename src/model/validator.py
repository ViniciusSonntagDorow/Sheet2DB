from abc import ABC, abstractmethod
import pandas as pd


class Validator(ABC):
    @abstractmethod
    def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
