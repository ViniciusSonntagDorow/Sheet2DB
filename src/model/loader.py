from abc import ABC, abstractmethod
import pandas as pd


class Loader(ABC):
    @abstractmethod
    def load_data(self, df: pd.DataFrame, destination: str) -> None:
        pass
