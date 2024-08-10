from fastapi import APIRouter, Depends
from app.services.income_service import IncomeService
from app.api.schemas.income_schema import IncomeCreate, IncomeResponse
from infra.dependency_injection.container import AppContainer as container

router = APIRouter()

def get_income_service() -> IncomeService:
    return container.income_service()

@router.post("/income/", response_model=IncomeResponse)
def create_income(income: IncomeCreate, income_service: IncomeService = Depends(get_income_service)):
    return income_service.create_income(income)

@router.get("/income/{income_id}", response_model=IncomeResponse)
def get_income(income_id: int, income_service: IncomeService = Depends(get_income_service)):
    return income_service.get_income(income_id)

@router.put("/income/{income_id}", response_model=IncomeResponse)
def update_income(income_id: int, income: IncomeCreate, income_service: IncomeService = Depends(get_income_service)):
    return income_service.update_income(income_id, income)

@router.delete("/income/{income_id}")
def delete_income(income_id: int, income_service: IncomeService = Depends(get_income_service)):
    return income_service.delete_income(income_id)