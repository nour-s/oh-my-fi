from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends
from app.domain.income import Income

from infra.repositories.income_repository import IncomeRepository

# Assuming IncomeRepository is imported from the appropriate module


class IncomeService:
    def __init__(self, income_repository: IncomeRepository = Depends()):
        self.income_repository = income_repository

    def create_income(self, title: str, amount: float, source: str, user_id: int) -> Income:
        return self.income_repository.create_income(title=title, amount=amount, source=source, user_id=user_id)

    def get_income_by_id(self, income_id: int) -> Income:
        return self.income_repository.get_income_by_id(income_id)

    def get_all_incomes(self) -> List[Income]:
        return self.income_repository.get_all_incomes()

    def update_income(self, income_id: int, title: str, amount: float, source: str) -> Income:
        return self.income_repository.update_income(income_id, title, amount, source)

    def delete_income(self, income_id: int) -> bool:
        return self.income_repository.delete_income(income_id)