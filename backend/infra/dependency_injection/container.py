from dependency_injector import containers, providers
from app.services.expense_service import ExpenseService
from infra.database.connection import get_db_session
from infra.repositories.expense_repository import ExpenseRepository

class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.api.endpoints.expenses_endpoints"])

    db_session = providers.Singleton(get_db_session)
    expense_repository = providers.Factory(ExpenseRepository, db=db_session)
    expense_service = providers.Factory(ExpenseService, expense_repository=expense_repository)