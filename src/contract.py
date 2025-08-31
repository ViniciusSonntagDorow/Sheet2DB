from pydantic import BaseModel, PositiveFloat
from datetime import datetime
from enum import Enum


class CategoryEnum(str, Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    ENTERTAINMENT = "entertainment"
    SHOPPING = "shopping"
    BILLS = "bills"
    HEALTH = "health"
    EDUCATION = "education"
    OTHER = "other"


class Statement(BaseModel):
    date: datetime
    description: str
    category: CategoryEnum
    amount: PositiveFloat
