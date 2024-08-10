
from decimal import Decimal
from pydantic import BaseModel, model_validator


class Money(BaseModel):
    amount: Decimal

    @model_validator(mode='after')
    def amount_must_be_non_negative(cls, values):
        amount = values.get('amount')
        if amount is not None and amount < 0:
            raise ValueError('Amount must be non-negative')
        return values

    class Config:
        frozen = True
