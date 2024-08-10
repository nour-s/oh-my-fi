# IncomeResponse
from pydantic import BaseModel
from typing import Optional

class IncomeResponse(BaseModel):
    id: int
    amount: float
    source: str
    date_received: Optional[str] = None

    class Config:
        from_attributes = True

# IncomeCreate
class IncomeCreate(BaseModel):
    amount: float
    source: str
    date_received: Optional[str] = None