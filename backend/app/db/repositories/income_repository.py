from sqlalchemy.orm import Session
from ..db.models.income import Income

class IncomeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_income(self, title: str, amount: float, source: str, user_id: int):
        new_income = Income(title=title, amount=amount, source=source, user_id=user_id)
        self.db.add(new_income)
        self.db.commit()
        self.db.refresh(new_income)
        return new_income

    def get_income_by_id(self, income_id: int):
        return self.db.query(Income).filter(Income.id == income_id).first()

    def get_all_incomes(self):
        return self.db.query(Income).all()

    def update_income(self, income_id: int, title: str, amount: float, source: str):
        income = self.get_income_by_id(income_id)
        if income:
            income.title = title
            income.amount = amount
            income.source = source
            self.db.commit()
            self.db.refresh(income)
            return income
        return None

    def delete_income(self, income_id: int):
        income = self.get_income_by_id(income_id)
        if income:
            self.db.delete(income)
            self.db.commit()
            return income
        return None
