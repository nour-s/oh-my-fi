import datetime

from app.domain.value_objects.money import Money


class Income:
    id: int
    amount: Money
    date: datetime
    description: str
    user_id: int
