from fastapi import FastAPI
from db.database import engine, Base
from api import user

app = FastAPI()

app.include_router(user.router)