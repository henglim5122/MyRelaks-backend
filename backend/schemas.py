from pydantic import BaseModel
from typing import Optional
from datetime import date

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

class Token(BaseModel):
    """Model for JWT token response."""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Model for JWT token data."""
    username: Optional[str] = None
