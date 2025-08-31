import pytest
from datetime import datetime
from src.contract import Statement, CategoryEnum
from pydantic import ValidationError


def test_statement_with_valid_data():
    """
    Test the creation of a Statement instance with valid data.
    """
    valid_data = {
        "date": datetime.now(),
        "description": "supermarket",
        "category": CategoryEnum.FOOD,
        "amount": 100.50,
    }

    statement = Statement(**valid_data)

    assert statement.date == valid_data["date"]
    assert statement.description == valid_data["description"]
    assert statement.category == valid_data["category"]
    assert statement.amount == valid_data["amount"]


def test_statement_with_invalid_data():
    """
    Test the creation of a Statement instance with invalid data.
    """
    invalid_data = {
        "date": "not a date",
        "description": "",
        "category": CategoryEnum.FOOD,
        "amount": -1,
    }

    with pytest.raises(ValidationError):
        Statement(**invalid_data)


def test_category_validation():
    """
    Test the validation of the category field.
    """
    data = {
        "date": datetime.now(),
        "description": "supermarket",
        "category": "unknown category",
        "amount": 100.50,
    }

    with pytest.raises(ValidationError):
        Statement(**data)
