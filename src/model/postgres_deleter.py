from sqlalchemy import create_engine, text

from utils.config import config


class PostgresDeleter:
    def __init__(self, connection_string: str = config.get_connection_string()):
        self.__connection_string = connection_string

    def delete_by_id(self, table_name: str, record_id: int) -> bool:
        engine = create_engine(self.__connection_string)
        with engine.connect() as conn:
            result = conn.execute(
                text(f"DELETE FROM {table_name} WHERE id = :id"), {"id": record_id}
            )
            conn.commit()
            return result.rowcount > 0

    def delete_by_ids(self, table_name: str, record_ids: list[int]) -> int:
        if not record_ids:
            return 0

        engine = create_engine(self.__connection_string)
        with engine.connect() as conn:
            result = conn.execute(
                text(f"DELETE FROM {table_name} WHERE id = ANY(:ids)"),
                {"ids": record_ids},
            )
            conn.commit()
            return result.rowcount
