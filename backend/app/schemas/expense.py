from pydantic import BaseModel

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(ExpenseBase):
    pass

class ExpenseInDB(ExpenseBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class ExpenseResponse:
    pass
