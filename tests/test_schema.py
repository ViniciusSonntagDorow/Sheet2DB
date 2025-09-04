import sys
import os

# Add the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
import numpy as np
import pandera.pandas as pa
import pytest

from src.schema import BaseSchema


def test_validated_schema():
    df_test = pd.DataFrame(
        {
            "date": ["erro", "2023-01-01", "2023-01-01"],
            "description": ["lidl", "pizza", "uber"],
            "category": ["Food", "Other", "Transport"],
            "amount": [10.0, 20.0, 5.0],
        }
    )

    BaseSchema.validate(df_test)


def test_extra_column():
    df_test = pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-01", "2023-01-01"],
            "description": ["lidl", "pizza", "uber"],
            "category": ["Food", "Other", "Transport"],
            "amount": [10.0, 20.0, 5.0],
            "extra_column": [0, 0, 0],
        }
    )

    with pytest.raises(pa.errors.SchemaError):
        BaseSchema.validate(df_test)


def test_missing_column():
    df_test = pd.DataFrame(
        {
            "description": ["lidl", "pizza", "uber"],
            "category": ["Food", "Other", "Transport"],
            "amount": [10.0, 20.0, 5.0],
        }
    )

    with pytest.raises(pa.errors.SchemaError):
        BaseSchema.validate(df_test)


def test_missing_value():
    df_test = pd.DataFrame(
        {
            "date": [np.nan, "2023-01-01", "2023-01-01"],
            "description": ["lidl", "pizza", "uber"],
            "category": ["Food", "Other", "Transport"],
            "amount": [10.0, 20.0, 5.0],
        }
    )

    with pytest.raises(pa.errors.SchemaError):
        BaseSchema.validate(df_test)


def test_invalid_category():
    df_test = pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-01", "2023-01-01"],
            "description": ["lidl", "pizza", "uber"],
            "category": ["invalid", "Other", "Transport"],
            "amount": [10.0, 20.0, 5.0],
        }
    )

    with pytest.raises(pa.errors.SchemaError):
        BaseSchema.validate(df_test)


def test_negative_amount():
    df_test = pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-01", "2023-01-01"],
            "description": ["lidl", "pizza", "uber"],
            "category": ["Food", "Other", "Transport"],
            "amount": [-10.0, 20.0, 5.0],
        }
    )

    with pytest.raises(pa.errors.SchemaError):
        BaseSchema.validate(df_test)


def test_invalid_date():
    df_test = pd.DataFrame(
        {
            "date": ["invalid_date", "2023-01-01", "2023-01-01"],
            "description": ["lidl", "pizza", "uber"],
            "category": ["Food", "Other", "Transport"],
            "amount": [10.0, 20.0, 5.0],
        }
    )

    with pytest.raises(pa.errors.SchemaError):
        BaseSchema.validate(df_test)
