from abc import ABC

from .interfaces import IRead


class BaseReader(IRead, ABC):
    def __init__(self, engine: str, dtype_backend: str):
        self.engine = engine
        self.dtype_backend = dtype_backend
