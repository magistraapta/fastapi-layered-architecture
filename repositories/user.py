from sqlalchemy.orm import Session
from models.user import User
from core.security import get_password_hash

class UserRepository:
    
    def create_user(self, user: User, db: Session):
        user.password = get_password_hash(user.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user
    
    def get_all_users(self, db: Session):
        return db.query(User).all()
    
    def get_user(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    
    def delete(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        
        if user:
            db.delete(user)
            db.commit()        
                
        return user