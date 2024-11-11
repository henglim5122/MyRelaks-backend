from .database import Base 
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean
from sqlalchemy.sql import func

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    gender = Column(String)
    user_type = Column(String, default="user")
    dob = Column(String, nullable=True)
    phone_code = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    city = Column(String, nullable=True)
    country = Column(String, nullable=True) 
    is_active = Column(Boolean, default=True)
    is_email_verified = Column(Boolean, default=False)
    updated_at = Column(DateTime, nullable=True)
    password_reset_token = Column(String, nullable=True)
    password_reset_expires = Column(DateTime, nullable=True)
    subscription = Column(Boolean, default=False)  
    tier = Column(String, default="Free") 