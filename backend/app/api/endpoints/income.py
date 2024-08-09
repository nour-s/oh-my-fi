from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.income import IncomeCreate, IncomeResponse
from app.services.income_service import IncomeService

router = APIRouter()

@router.post("/income/", response_model=IncomeResponse)
def create_income(income: IncomeCreate, db: Session = Depends(get_db)):
    return IncomeService.create_income(db, income)

@router.get("/income/{income_id}", response_model=IncomeResponse)
def get_income(income_id: int, db: Session = Depends(get_db)):
    return IncomeService.get_income(db, income_id)

@router.put("/income/{income_id}", response_model=IncomeResponse)
def update_income(income_id: int, income: IncomeCreate, db: Session = Depends(get_db)):
    return IncomeService.update_income(db, income_id, income)

@router.delete("/income/{income_id}")
def delete_income(income_id: int, db: Session = Depends(get_db)):
    return IncomeService.delete_income(db, income_id)
