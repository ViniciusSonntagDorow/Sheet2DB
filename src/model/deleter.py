from abc import ABC, abstractmethod


class Deleter(ABC):
    @abstractmethod
    def delete_by_id(self, table_name: str, record_id: int) -> bool:
        pass

    @abstractmethod
    def delete_by_ids(self, table_name: str, record_ids: list[int]) -> int:
        pass
