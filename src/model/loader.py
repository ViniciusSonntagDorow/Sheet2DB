from abc import ABC, abstractmethod
import pandas as pd


class Loader(ABC):
    @abstractmethod
    def load_data(self, df: pd.DataFrame, table_name: str) -> None:
        pass
