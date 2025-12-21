import pandera.pandas as pa
from pandera.typing import Series

# import pandas as pd
# from typing import Optional
from utils.config import config


class BaseSchema(pa.DataFrameModel):
    expense_date: Series[pa.DateTime]
    description: Series[str]
    # description: Series[Optional[str]] = pa.Field(nullable=True) # If needed, we can specify a nullable collumn
    category: Series[str] = pa.Field(isin=config.VALID_CATEGORIES)
    amount: Series[float] = pa.Field(ge=0)  # Greater or equal to 0

    class Config:
        """Apply strict and coerce to all columns"""

        strict = True  # Dataframe needs to have all the columns defined in the schema
        coerce = True  # Try to convert the data to the correct type

    # Example of a custom check (This one does the same as the isin check above)
    # @pa.check(
    #         "category",
    #         name = "Checking category",
    #         error = "Invalid category")
    # def checking_category(cls, category: Series[str]) -> Series[bool]:
    #     return category.isin(["Food", "Transport", "Entertainment", "Shopping", "Bills", "Health", "Education", "Other"])
    #     return codigo.str[:4].isin(['REP_', 'MNT_', 'VND_']) # Another example of a custom check
