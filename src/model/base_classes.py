from abc import ABC

from .interfaces import IRead


class BaseReader(IRead, ABC):
    """
    An abstract base class for file readers that share common
    pandas configurations (engine and dtype_backend).

    This class provides the shared __init__ logic to store
    these settings. Concrete subclasses are still responsible
    for implementing the abstract `read_data` method from IRead.
    """

    def __init__(self, engine: str, dtype_backend: str):
        """
        Initializes the BaseReader with shared configurations.

        Args:
            engine (str): The pandas parser engine to use (e.g., 'c', 'pyarrow', 'calamine').
            dtype_backend (str): The backend for data types (e.g., 'numpy_nullable', 'pyarrow').
        """
        self.engine = engine
        self.dtype_backend = dtype_backend
