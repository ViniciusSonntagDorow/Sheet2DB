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

# function that treats the error message for a better user experience. 

def format_pandera_errors(exc: pa.errors.SchemaErrors) -> str:
    formatted_errors = []
    schema_errors = exc.schema_errors

    # Error for mandatory columns that are missing from the file
    if "COLUMN_NOT_IN_DATAFRAME" in schema_errors:
        missing_columns = [e["column"] for e in schema_errors["COLUMN_NOT_IN_DATAFRAME"]]
        formatted_errors.append(
            f"Mandatory columns not found: **{', '.join(missing_columns)}**."
        )

    # Error for columns that exist in the file but are not part of the schema
    if "COLUMN_NOT_IN_SCHEMA" in schema_errors:
        extra_columns = [e["column"] for e in schema_errors["COLUMN_NOT_IN_SCHEMA"]]
        formatted_errors.append(
            f"Unexpected columns found: **{', '.join(extra_columns)}**. Please remove them."
        )

    df_failure_cases = exc.failure_cases
    if not df_failure_cases.empty:
        if formatted_errors:  # Adds a separator if there were column errors
            formatted_errors.append("---")
        formatted_errors.append("Errors were found in the following data:")

        # Group errors by column and check type to avoid repetitive messages
        for (column, check), group in df_failure_cases.groupby(['column', 'check'], dropna=False):
            first_error = group.iloc[0]

            failure_case = first_error.get('failure_case', '[value unavailable]')
            index_label = first_error.get('index', '[unknown row]')

            # Ensures the row is displayed as a number, if possible
            try:
                row_number = int(index_label) + 2
            except (ValueError, TypeError):
                row_number = index_label

            if "isin" in str(check):
                msg = f"  - In column **'{column}'**, the value '**{failure_case}**' (row {row_number}) is not a valid category."
            elif "greater_than_or_equal_to" in str(check):
                msg = f"  - In column **'{column}'**, the value **{failure_case}** (row {row_number}) is invalid. The value cannot be negative."
            elif "invalid_type" in str(check):
                msg = f"  - In column **'{column}'**, the value '**{failure_case}**' (row {row_number}) is not in the expected format (e.g., invalid date)."
            else:
                msg = f"  - Error in column **'{column}'** (row {row_number}): the value '**{failure_case}**' is invalid."

            # Append a count if there are more errors of the same type
            if len(group) > 1:
                msg += f" (and in **{len(group) - 1}** other rows)"

            formatted_errors.append(msg)

    return "\n".join(formatted_errors)

def process_excel(
    uploaded_file: str,
) -> Tuple[Optional[pd.DataFrame], bool, Optional[str]]:
    df = pd.read_excel(uploaded_file)
    try:
        BaseSchema.validate(df, lazy=True)
        return df, True, None

    except pa.errors.SchemaErrors as exc:
        error_message = format_pandera_errors(exc)
        return None, False, error_message

    except Exception as e:
        return None, False, f"Unexpected error: {str(e)}"


def excel_to_sql(df: pd.DataFrame) -> None:
    df.to_sql("statements", con=DATABASE_URL, if_exists="append", index=False)
