from sqlalchemy.orm import Session
from models.user import User

class UserRepository:
    
    def create_user(self, user: User, db: Session):
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user
    
    def get_all_users(self, db: Session):
        return db.query(User).all()