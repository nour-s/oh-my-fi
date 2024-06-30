from sqlalchemy.orm import Session
from ..db.repositories.expense_repository import ExpenseRepository
from ..schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseInDB

class ExpenseService:
    def __init__(self, db: Session):
        self.db = db
        self.expense_repository = ExpenseRepository(db)

    def create_expense(self, expense: ExpenseCreate, user_id: int):
        return self.expense_repository.create_expense(
            title=expense.title,
            amount=expense.amount,
            category=expense.category,
            user_id=user_id
        )

    def get_expense_by_id(self, expense_id: int):
        return self.expense_repository.get_expense_by_id(expense_id)

    def get_expenses_by_user(self, user_id: int):
        return self.expense_repository.get_expenses_by_user(user_id)

    def update_expense(self, expense_id: int, expense: ExpenseUpdate):
        return self.expense_repository.update_expense(
            expense_id=expense_id,
            title=expense.title,
            amount=expense.amount,
            category=expense.category
        )

    def delete_expense(self, expense_id: int):
        return self.expense_repository.delete_expense(expense_id)
