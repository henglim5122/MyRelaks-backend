from database import Base 
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean, Text, Float,JSON
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
    last_login = Column(DateTime(timezone=True), nullable=True)
    is_email_verified = Column(Boolean, default=False)
    updated_at = Column(DateTime, nullable=True)
    password_reset_token = Column(String(128), nullable=True, index=True)
    password_reset_expires = Column(DateTime(timezone=True), nullable=True)
    subscription = Column(Boolean, default=False)  
    tier = Column(String, nullable=True,default=None) 
    subscription_time = Column(DateTime, nullable=True)
    subscription_expire = Column(DateTime, nullable=True)
    points = Column(Integer, nullable=True,default=None)


class Destination(Base):
    __tablename__ = "destination"
    
    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String(255), index=True, nullable=False)  
    location = Column(String(255), index=True, nullable=False)  
    state = Column(String(100), index=True, nullable=False)  
    coordinate = Column(JSON, nullable=True)  
    description = Column(String, nullable=True)  
    reviewRating = Column(Float, nullable=True)  
    activityCategory = Column(String(100), nullable=True)  
    src = Column(String(255), nullable=True)  
    openingHours = Column(String(100), nullable=True)  
    minPrice = Column(Float, nullable=True)  
    maxPrice = Column(Float, nullable=True)  
    


class Payment(Base):
    __tablename__ = "payment_information"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    aspect = Column(String)
    payment_amount = Column(Float)
    payment_method = Column(String)
    payment_status = Column(String, default="Pending")
    payment_date = Column(DateTime, default=func.now())
    encrypted_payment_info = Column(String,unique=True)


class Itinerary_Record(Base):
    __tablename__ = "itinerary_record"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    trip_name = Column(String)
    trip_ai_record = Column(JSON)
    total_budget = Column(Float)
    estimated_cost = Column(Float)

  
class CustomerPreference(Base):
    __tablename__ = "customer_preference"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    destination_id = Column(Integer, ForeignKey("destination.id"))

