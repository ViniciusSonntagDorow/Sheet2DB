from abc import ABC, abstractmethod
import pandas as pd


class Transformer(ABC):
    @abstractmethod
    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
