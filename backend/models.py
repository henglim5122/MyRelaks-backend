from database import Base 
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean, Text
from sqlalchemy.sql import func

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    profile_image = Column(Text, nullable=True)
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
    password_reset_token = Column(String(128), nullable=True, index=True)
    password_reset_expires = Column(DateTime(timezone=True), nullable=True)
    subscription = Column(Boolean, default=False)  
    tier = Column(String, default="Free") 


class Destination(Base):
    __tablename__ = "destination"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    state = Column(String, index=True)
    description = Column(String)
    coordinates = Column(String, nullable=True)
    rating = Column(Integer, unique=True)
    min_price = Column(Integer, nullable=True)
    max_prce = Column(Integer, nullable=True)
    src = Column(String, nullable=True)
    liked_by = Column(Boolean, default=False)


class Payment(Base):
    __tablename__ = "payment_information"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    aspect = Column(String)
    payment_amount = Column(Integer)
    payment_method = Column(String)
    payment_status = Column(String, default="Pending")
    payment_date = Column(DateTime, default=func.now())
    encrypted_payment_info = Column(String,unique=True)


class Itinerary_Record(Base):
    __tablename__ = "itinerary_record"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    trip_name = Column(String)
    trip_dates = Column(Date)
    total_budget = Column(Integer)
    estimated_cost = Column(Integer)