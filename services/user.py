from sqlalchemy.orm import Session
from repositories.user import UserRepository
from schemas.user import UserCreate
from models.user import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        
    def create_user(self, user_create: UserCreate, db: Session):
        user = User(
            username = user_create.username,
            password = user_create.password
        )
        
        return self.user_repository.create_user(user=user, db=db)
    
    def get_all_users(self, db: Session):
        return self.user_repository.get_all_users(db=db)