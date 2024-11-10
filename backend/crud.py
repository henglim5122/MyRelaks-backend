from sqlalchemy.orm import Session
from models import Users
from schemas import UserCreate

# Create a new user
def create_user(db: Session, user: UserCreate):
    new_user = Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get a user by ID
def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Users).offset(skip).limit(limit).all()

# Update a user's email
def update_user_email(db: Session, user_id: int, new_email: str):
    user = get_user(db, user_id)
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
        return user
    return None

# Delete a user by ID
def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
