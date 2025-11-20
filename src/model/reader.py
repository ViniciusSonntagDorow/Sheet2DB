from abc import ABC, abstractmethod
import pandas as pd


class Reader(ABC):
    @abstractmethod
    def read_data(self, file: str) -> pd.DataFrame:
        pass
