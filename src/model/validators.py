import pandas as pd
import pandera.pandas as pa

from .interfaces import IValidate
from .schema import BaseSchema


class PanderaValidator(IValidate):
    def __init__(self, schema: pa.DataFrameSchema = BaseSchema):
        self.schema = schema

    def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            validated_df = self.schema.validate(df, lazy=True)
            return validated_df
        except pa.errors.SchemaErrors as e:
            return pd.DataFrame()
