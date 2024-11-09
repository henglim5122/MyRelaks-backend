"""
This module handles user authentication and authorization, including registration and login.
"""

# Standard library imports
import os
from datetime import date, timedelta, datetime, timezone
from typing import Annotated, Optional

# Third-party imports
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError

# Local application imports
from models import Users
from database import get_db

# Load environment variables from the .env file in the backend directory
load_dotenv()

# Initialize API router
router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Load secret key and algorithm from environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
if not SECRET_KEY or not ALGORITHM:
    raise RuntimeError("Environment variables SECRET_KEY or ALGORITHM are not set.")

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="login")
access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "20"))


class UserBase(BaseModel):
    """
    Base model for user details.
    """

    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    gender: str
    user_type: str
    dob: Optional[date] = None
    phone_code: Optional[str] = None
    phone_number: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    subscription: bool
    tier: str
    is_active: bool
    is_email_verified: bool

    class Config:  # pylint: disable=too-few-public-methods
        """
        Pydantic configuration class for enabling ORM mode.
        """

        orm_mode = True


class UserRequest(BaseModel):
    """
    Model for user registration requests.
    """

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


class Token(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Pydantic model for representing a JWT token response.
    """

    access_token: str
    token_type: str


def authenticate_user(username: str, password: str, db: Session):
    """
    Authenticate the user by verifying the provided username and password.
    """
    user = db.query(Users).filter(Users.username == username).first()
    if (
        not user
        or not user.hashed_password
        or not bcrypt_context.verify(password, user.hashed_password)
    ):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    """
    Create a JWT access token with a specified expiration time.
    """
    to_encode = {"sub": username, "id": user_id}
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    """
    Endpoint to log in a user and return a JWT token.
    """
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token(
        user.username, user.id, timedelta(minutes=access_token_expire_minutes)
    )
    return {"access_token": token, "token_type": "bearer"}


@router.get("/user", response_model=UserBase)
async def get_current_user(
    token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency
):
    """
    Get the current authenticated user based on the JWT token.
    """
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
    except ExpiredSignatureError as exc:
        raise HTTPException(status_code=401, detail="Token has expired") from exc
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Could not validate user") from exc


@router.put("/user/{user_id}", response_model=UserBase)
async def update_user(user_id: int, user_update: UserRequest, db: db_dependency):
    """
    Update a user's information by their ID.
    """
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


@router.delete("/user/{user_id}", status_code=200)
async def delete_user(user_id: int, db: db_dependency):
    """
    Delete a user by their ID.
    """
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"msg": "User deleted successfully"}
