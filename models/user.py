from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from db.database import Base


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)