from fastapi import FastAPI

from app.api.endpoints import expenses_endpoints, income_endpoints
from app.core.config import settings
from infra.dependency_injection.container import AppContainer


app = FastAPI()


# Create the container
container = AppContainer()

# Wire the container with the FastAPI app
container.wire(modules=[expenses_endpoints])

# Include the router
app.include_router(expenses_endpoints.router)

app.include_router(expenses_endpoints.router, prefix="/api/v1/expenses", tags=["expenses"])
app.include_router(income_endpoints.router, prefix="/api/v1/income", tags=["income"])
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)
