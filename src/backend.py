import pandas as pd
import pandera.pandas as pa
from schema import BaseSchema
from dotenv import load_dotenv
import os
from typing import Tuple, Optional

load_dotenv(".env")

# Read the environment variables
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Create the database URL
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def process_excel(
    uploaded_file: str,
) -> Tuple[Optional[pd.DataFrame], bool, Optional[str]]:
    df = pd.read_excel(uploaded_file)
    try:
        BaseSchema.validate(df, lazy=True)
        return df, True, None

    except pa.errors.SchemaErrors as exc:
        return None, False, str(exc)
    except Exception as e:
        return None, False, f"Unexpected error: {str(e)}"


def excel_to_sql(df: pd.DataFrame) -> None:
    df.to_sql("statements", con=DATABASE_URL, if_exists="append", index=False)
