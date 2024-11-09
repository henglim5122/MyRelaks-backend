from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    gender: str
    user_type: str = "user"
    dob: Optional[date]
    phone_code: Optional[str]
    phone_number: Optional[str]
    city: Optional[str]
    country: Optional[str]
    is_active: bool = True
    is_email_verified: bool = False
    subscription: bool = False
    tier: str = "Free"

class UserCreate(UserBase):
    hashed_password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
