import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from models import Users
from database import SessionLocal
from typing import Annotated, Optional, List
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import date, timedelta, datetime, timezone

load_dotenv(dotenv_path="./../frontend/.env")

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Pydantic model for user
class UserBase(BaseModel):
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

    class Config:
        orm_mode = True  

# User Registration Model
class UserRequest(BaseModel):  
    first_name: str
    last_name: str
    username: str
    password: str
    email: str
    gender: str
    dob: Optional[date] = None  # Optional fields can be marked as Optional
    phone_code: Optional[str] = None
    phone_number: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

@router.post("/register")
async def register_user(db: db_dependency, user_request: UserRequest):
    try:
        user = Users(
            username=user_request.username,
            first_name=user_request.first_name,
            last_name=user_request.last_name,
            hashed_password=bcrypt_context.hash(user_request.password),
            user_type="user",
            email=user_request.email,
            gender=user_request.gender,
            dob=user_request.dob,
            phone_code=user_request.phone_code,
            phone_number=user_request.phone_number,
            city=user_request.city,
            country=user_request.country,
            subscription=False,
            tier='Free'
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"msg": "User registered successfully", "user_id": user.id}
    except Exception as e:
        db.rollback()  # Ensure no partial commits are left
        raise HTTPException(status_code=500, detail=str(e)) 

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="login")

class Token(BaseModel):
    access_token: str
    token_type: str

def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login", response_model=Token)  # Login endpoint
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status_code=401, detail="Could not validate user.")
    else:
        token = create_access_token(user.username, user.id, timedelta(minutes=20))
        return {"access_token": token, "token_type": "bearer"}

@router.get("/user", response_model=UserBase)
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=401, detail="Could not validate user.")
        
        user = db.query(Users).filter(Users.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Could not validate user.")
        
        return user  # The UserBase model now returns additional fields
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate user.")
    
@router.get("/user/{user_id}", response_model=UserBase)
async def get_user(user_id: int, db: db_dependency):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/user/{user_id}", response_model=UserBase)
async def update_user(user_id: int, user_update: UserRequest, db: db_dependency):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_data = user_update.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    return user

@router.delete("/user/{user_id}", status_code=200)
async def delete_user(user_id: int, db: db_dependency):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return None