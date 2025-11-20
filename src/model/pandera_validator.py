import pandas as pd
import pandera.pandas as pa

from utils.validation_error import ValidationError
from utils.schema import BaseSchema
from model.validator import Validator


class PanderaValidator(Validator):
    def __init__(self, schema: pa.DataFrameSchema = BaseSchema):
        self.__schema = schema

    def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            return self.__schema.validate(df, lazy=True)
        except pa.errors.SchemaErrors as e:
            raise ValidationError(f"Data validation failed: {e}")

        except Exception as e:
            raise ValidationError(f"Unexpected error during validation: {e}")
