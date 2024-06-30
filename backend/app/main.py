from fastapi import FastAPI

from app.api.v1.endpoints import expenses, income, auth
from app.core.config import settings
from app.db.session import engine

app = FastAPI()

app.include_router(expenses.router, prefix="/api/v1/expenses", tags=["expenses"])
app.include_router(income.router, prefix="/api/v1/income", tags=["income"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)
