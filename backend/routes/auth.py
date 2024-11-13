"""
This module handles user authentication and authorization, including registration and login.
"""

import os
from datetime import timedelta, datetime, timezone
from typing import Annotated, Optional
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError

# Local application imports
from ..models import Users
from ..database import get_db
from ..schemas import Token, TokenData, UserBase, UserRequest

# Load environment variables
load_dotenv()

# Initialize API router and dependencies
router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "20"))

# OAuth2 settings
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="login")

# Helper functions
def authenticate_user(username: str, password: str, db: Session):
    """Authenticate the user by verifying the provided username and password."""
    user = db.query(Users).filter(Users.username == username).first()
    if not user or not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    """Create a JWT access token with an expiration time."""
    to_encode = {"sub": username, "id": user_id}
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Authentication endpoints
@router.post("/register", tags=["Authorization"])
async def register_user(db: db_dependency, user_request: UserRequest):
    """Register a new user."""
    existing_user = db.query(Users).filter(Users.username == user_request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    user = Users(
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        username=user_request.username,
        hashed_password=bcrypt_context.hash(user_request.password),
        email=user_request.email,
        gender=user_request.gender,
        dob=user_request.dob,
        phone_code=user_request.phone_code,
        phone_number=user_request.phone_number,
        city=user_request.city,
        country=user_request.country,
        subscription=False,
        tier="Free",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "User registered successfully", "user_id": user.id}

@router.post("/login", response_model=Token, tags=["Authorization"])
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    """Login and return a JWT token."""
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token(
        user.username, user.id, timedelta(minutes=access_token_expire_minutes)
    )
    return {"access_token": token, "token_type": "bearer"}

@router.get("/user", response_model=UserBase, tags=["User"])
async def get_current_user(
    token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency
):
    """Get the current authenticated user based on the JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        user_id = payload.get("id")

        if username is None or user_id is None:
            raise HTTPException(status_code=401, detail="Could not validate user")

        user = db.query(Users).filter(Users.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Could not validate user")

        return user
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate user")
