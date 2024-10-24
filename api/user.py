from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserRead
from db.database import get_db
from repositories.user import UserRepository
from services.user import UserService
from typing import List

router = APIRouter(prefix='/users', tags=['users'])

user_repository = UserRepository()
user_service = UserService(user_repository=user_repository)

@router.post("/", response_model=UserCreate)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    
    return user_service.create_user(user_create, db)

@router.get("/", response_model=List[UserRead])
def get_all_users(db: Session = Depends(get_db)):
    
    return user_service.get_all_users(db)

@router.get("/test")
def test():
    return {"test": "testing"}
