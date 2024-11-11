from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# User Schemas
class UserBase(BaseModel):
    """Base model for user details."""
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    gender: str
    user_type: Optional[str] = "user"
    dob: Optional[date] = None
    phone_code: Optional[str] = None
    phone_number: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    subscription: Optional[bool] = False
    tier: Optional[str] = "Free"
    is_active: bool = True
    is_email_verified: bool = False

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str

class UserRequest(BaseModel):
    """Model for user registration requests."""
    first_name: str
    last_name: str
    username: str
    password: str
    email: str
    gender: str
    dob: Optional[date] = None
    phone_code: Optional[str] = None
    phone_number: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

class UserResponse(BaseModel):
    """Model for user response data."""
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    gender: Optional[str] = None
    dob: Optional[date] = None
    phone_code: Optional[str] = None
    phone_number: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    subscription: Optional[bool] = False
    tier: Optional[str] = "Free"
    is_active: bool = True
    is_email_verified: bool = False

    class Config:
        orm_mode = True

# Destination Schemas
class DestinationBase(BaseModel):
    """Base model for destination details."""
    destination_id: int
    name: str
    location: str
    state: Optional[str] = None
    description: Optional[str] = None
    coordinates: Optional[str] = None
    ratings_review: Optional[float] = None
    price: Optional[float] = None

    class Config:
        from_attributes = True

class DestinationCreate(BaseModel):
    """Model for creating a new destination."""
    name: str
    location: str
    state: Optional[str] = None
    description: Optional[str] = None
    coordinates: Optional[str] = None
    ratings_review: Optional[float] = None
    price: Optional[float] = None

class DestinationResponse(BaseModel):
    """Model for destination response data."""
    destination_id: int
    name: str
    location: str
    state: Optional[str] = None
    description: Optional[str] = None
    coordinates: Optional[str] = None
    ratings_review: Optional[float] = None
    price: Optional[float] = None

    class Config:
        orm_mode = True

# Itinerary Schemas
class ItineraryBase(BaseModel):
    """Base model for itinerary details."""
    itinerary_id: int
    users_id: int
    destination_id: int
    trip_name: str
    trip_dates: Optional[str] = None
    activities: Optional[str] = None
    total_budget: Optional[float] = None
    estimated_cost: Optional[float] = None

    class Config:
        from_attributes = True

class ItineraryCreate(BaseModel):
    """Model for creating a new itinerary."""
    users_id: int
    destination_id: int
    trip_name: str
    trip_dates: Optional[str] = None
    activities: Optional[str] = None
    total_budget: Optional[float] = None
    estimated_cost: Optional[float] = None

class ItineraryResponse(BaseModel):
    """Model for itinerary response data."""
    itinerary_id: int
    users_id: int
    destination_id: int
    trip_name: str
    trip_dates: Optional[str] = None
    activities: Optional[str] = None
    total_budget: Optional[float] = None
    estimated_cost: Optional[float] = None

    class Config:
        orm_mode = True

# Token Schemas
class Token(BaseModel):
    """Model for JWT token response."""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Model for JWT token data."""
    username: Optional[str] = None
