from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter()

@router.get("/auth/")
def authenticate_user(current_user: str = Depends(get_current_user)):
    return {"message": f"Authenticated user: {current_user}"}
