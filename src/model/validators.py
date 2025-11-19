import pandas as pd
import pandera.pandas as pa

from exceptions.validation import ValidationError
from model.interfaces import IValidate
from model.schema import BaseSchema


class PanderaValidator(IValidate):
    def __init__(self, schema: pa.DataFrameSchema = BaseSchema):
        self.schema = schema

    def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            return self.schema.validate(df, lazy=True)
        except pa.errors.SchemaErrors as e:
            raise ValidationError(f"Data validation failed: {e}")

        except Exception as e:
            raise ValidationError(f"Unexpected error during validation: {e}")
