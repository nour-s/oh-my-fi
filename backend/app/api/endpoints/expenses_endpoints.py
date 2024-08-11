from fastapi import APIRouter, Depends
from app.services.expense_service import ExpenseService
from app.api.schemas.expense_schema import ExpenseCreate, ExpenseResponse
from infra.dependency_injection.container import AppContainer
from dependency_injector.wiring import Provide, inject
from infra.dependency_injection.container import AppContainer

router = APIRouter()

@router.post("/expenses/", response_model=ExpenseResponse)
@inject
def create_expense(expense: ExpenseCreate, expense_service: ExpenseService = Depends(Provide[AppContainer.expense_service])):
    return expense_service.create_expense(expense)

@router.get("/expenses/{expense_id}", response_model=ExpenseResponse)
@inject
def get_expense(expense_id: int, expense_service: ExpenseService = Depends(Provide[AppContainer.expense_service])):
    return expense_service.get_expense_by_id(expense_id)

@router.put("/expenses/{expense_id}", response_model=ExpenseResponse)
@inject
def update_expense(expense_id: int, expense: ExpenseCreate, expense_service: ExpenseService = Depends(Provide[AppContainer.expense_service])):
    return expense_service.update_expense(expense_id, expense)

@router.delete("/expenses/{expense_id}")
@inject
def delete_expense(expense_id: int, expense_service: ExpenseService = Depends(Provide[AppContainer.expense_service])):
    return expense_service.delete_expense(expense_id)