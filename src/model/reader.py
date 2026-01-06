from abc import ABC, abstractmethod
import pandas as pd


class Reader(ABC):
    @abstractmethod
    def read_data(self, query: str) -> pd.DataFrame:
        pass
