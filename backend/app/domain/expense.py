import datetime
from decimal import Decimal
from pydantic import BaseModel, root_validator

from .value_objects.money import Money  # Import root_validator

class Expense(BaseModel):
    id: int
    amount: Money
    date: datetime
    description: str
    category_id: int
    user_id: int

    class Config:
        arbitrary_types_allowed = True