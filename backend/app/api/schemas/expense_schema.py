import datetime
from pydantic import BaseModel

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str
    date: datetime

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        
class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True 