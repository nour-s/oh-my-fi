from fastapi import APIRouter, Depends
from app.services.expense_service import ExpenseService
from app.api.schemas.expense_schema import ExpenseCreate, ExpenseResponse
from infra.dependency_injection.container import AppContainer as container

router = APIRouter()

def get_expense_service() -> ExpenseService:
    return container.expense_service()

@router.post("/expenses/", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, expense_service: ExpenseService = Depends(get_expense_service)):
    return expense_service.create_expense(expense)

@router.get("/expenses/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int, expense_service: ExpenseService = Depends(get_expense_service)):
    return expense_service.get_expense_by_id(expense_id)

@router.put("/expenses/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, expense: ExpenseCreate, expense_service: ExpenseService = Depends(get_expense_service)):
    return expense_service.update_expense(expense_id, expense)

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, expense_service: ExpenseService = Depends(get_expense_service)):
    return expense_service.delete_expense(expense_id)