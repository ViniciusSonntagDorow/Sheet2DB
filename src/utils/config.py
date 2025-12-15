import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(find_dotenv())


class Config:
    # Database Configuration
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    # File paths
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = BASE_DIR / "data"

    # File processing settings
    CSV_SEPARATOR = ","
    CSV_ENCODING = "utf-8"
    CSV_ENGINE = "pyarrow"
    EXCEL_ENGINE = "calamine"
    DTYPE_BACKEND = "pyarrow"

    # Valid categories
    VALID_CATEGORIES = [
        "Supermarket",
        "Transport",
        "Entertainment",
        "Shopping",
        "Bills",
        "Health",
        "Education",
        "Other",
    ]

    # Database table name
    POSTGRES_TABLE = os.getenv("POSTGRES_TABLE")

    @classmethod
    def get_connection_string(cls) -> str:
        return f"postgresql://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}@{cls.POSTGRES_HOST}:{cls.POSTGRES_PORT}/{cls.POSTGRES_DB}"


config = Config()
