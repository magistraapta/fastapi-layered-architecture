from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    

class UserUpdate(BaseModel):
    username: Optional[str] = None  # `username` is optional
    password: Optional[str] = None 

    class Config:
        orm_mode = True
