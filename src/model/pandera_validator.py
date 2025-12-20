import pandas as pd
import pandera.pandas as pa

from utils.schema import BaseSchema
from model.validator import Validator


class PanderaValidator(Validator):
    def __init__(self, schema: pa.DataFrameSchema = BaseSchema):
        self.__schema = schema

    def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.__schema.validate(df, lazy=True)
