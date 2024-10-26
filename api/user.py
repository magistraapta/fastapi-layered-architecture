from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse, UserUpdate
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

@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    
    return user_service.get_all_users(db)

@router.get("/test")
def test():
    return {"test": "testing"}

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db=db, user_id=user_id)
    
    if not user:
        return HTTPException(status_code=404, detail="user not found")
    
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = user_service.update_user(user_id=user_id, username=user.username, db=db)
    
    if not updated_user:
        return HTTPException(status_code=404, detail="user not found")
    
    return updated_user

@router.delete("/delete/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = user_service.delete_user(db=db, user_id=user_id)
    
    if not delete_user:
        return HTTPException(status_code=404, detail="user not found")
    
    return deleted_user