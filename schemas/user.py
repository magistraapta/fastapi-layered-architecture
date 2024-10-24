from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    username: str

    class Config:
        orm_mode = True
