from .database import Base 
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Boolean, Float, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

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

    # Relationships
    itineraries = relationship("ItineraryData", back_populates="user")
    payments = relationship("PaymentData", back_populates="user")

class DestinationData(Base):
    __tablename__ = "destination_data"
    
    destination_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    state = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    coordinates = Column(String, nullable=True)
    ratings_review = Column(Float, nullable=True)
    price = Column(Float, nullable=True)
    liked_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Relationships
    itineraries = relationship("ItineraryData", back_populates="destination")
    liked_by_user = relationship("Users", back_populates="destinations")

class ItineraryData(Base):
    __tablename__ = "itinerary_data"
    
    itinerary_id = Column(Integer, primary_key=True, index=True)
    users_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    destination_id = Column(Integer, ForeignKey("destination_data.destination_id"), nullable=False)
    trip_name = Column(String, nullable=False)
    trip_dates = Column(String, nullable=True)
    activities = Column(Text, nullable=True)
    total_budget = Column(Float, nullable=True)
    estimated_cost = Column(Float, nullable=True)

    # Relationships
    user = relationship("Users", back_populates="itineraries")
    destination = relationship("DestinationData", back_populates="itineraries")

