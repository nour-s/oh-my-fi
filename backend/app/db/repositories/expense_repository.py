from sqlalchemy.orm import Session
from ..db.models.expense import Expense

class ExpenseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_expense(self, title: str, amount: float, category: str, user_id: int):
        new_expense = Expense(title=title, amount=amount, category=category, user_id=user_id)
        self.db.add(new_expense)
        self.db.commit()
        self.db.refresh(new_expense)
        return new_expense

    def get_expense_by_id(self, expense_id: int):
        return self.db.query(Expense).filter(Expense.id == expense_id).first()

    def get_expenses_by_user(self, user_id: int):
        return self.db.query(Expense).filter(Expense.user_id == user_id).all()

    def update_expense(self, expense_id: int, title: str, amount: float, category: str):
        expense = self.get_expense_by_id(expense_id)
        if expense:
            expense.title = title
            expense.amount = amount
            expense.category = category
            self.db.commit()
            self.db.refresh(expense)
            return expense
        return None

    def delete_expense(self, expense_id: int):
        expense = self.get_expense_by_id(expense_id)
        if expense:
            self.db.delete(expense)
            self.db.commit()
            return expense
        return None
