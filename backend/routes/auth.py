import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, constr, field_validator
from models import Users
from database import SessionLocal
from typing import Annotated, Optional, List
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import date, timedelta, datetime, timezone
import secrets

load_dotenv()

auth_router = APIRouter(tags=["Authorization"])
user_router = APIRouter(tags=["User"])

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
    profile_image: Optional[str] = None
    email: str
    gender: str
    user_type: Optional[str] = "user"
    dob: Optional[str] = None
    phone_code: Optional[str] = None
    phone_number: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    subscription: Optional[bool] = False
    tier: Optional[str] = None
    last_login: Optional[datetime] = None
    is_email_verified: bool
    points: Optional[int] = 0

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat() if dt else None
        }

# User Registration Model
class UserRequest(BaseModel):  
    first_name: str
    last_name: str
    username: str
    profile_image: Optional[str] = None
    password: str
    email: str
    gender: str
    dob: str
    phone_code: Optional[str] = None
    phone_number: str
    city: str
    country: str
    # dob: Optional[str] = None  
    # phone_code: Optional[str] = None
    # phone_number: Optional[str] = None
    # city: Optional[str] = None
    # country: Optional[str] = None
    
class ForgotPasswordRequest(BaseModel):
    email: str

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str

@auth_router.post("/register")
async def register_user(db: db_dependency, user_request: UserRequest):
    
    try:
        user = Users(
            first_name=user_request.first_name,
            last_name=user_request.last_name,
            username=user_request.username,
            profile_image = user_request.profile_image,
            hashed_password=bcrypt_context.hash(user_request.password),
            email=user_request.email,
            gender=user_request.gender,
            user_type="user",      
            dob=user_request.dob,
            phone_code=user_request.phone_code,
            phone_number=user_request.phone_number,
            city=user_request.city,
            country=user_request.country,
            subscription=False,
            tier=None,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        print(user_request)
        return {"msg": "User registered successfully", "user_id": user}
    except Exception as e:
        db.rollback()  # Ensure no partial commits are left
        raise HTTPException(status_code=500, detail=str(e)) 

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

def authenticate_user(username: str, password: str, db):
    # print(username, password)
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    # print(user)
    return user
    

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

@auth_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Could not validate user.")
    token = create_access_token(user.username, user.id, timedelta(minutes=120))
    return {"access_token": token, "token_type": "bearer"}

@user_router.get("/user", response_model=UserBase)
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        
        if username is None or user_id is None:
            raise HTTPException(status_code=401, detail="Could not validate user.")
        
        user = db.query(Users).filter(Users.id == user_id).first()
        
        db.commit()
        db.refresh(user)
        if user is None:
            raise HTTPException(status_code=401, detail="Could not validate user.")
        
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate user.")
        

@user_router.get("/user/{user_id}", response_model=UserBase)
async def get_user(user_id: int, db: db_dependency):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/user/{user_id}/{email}/add_points/")
async def update_user_points(user_id: int, email: str, points: int, db: db_dependency):
    user = db.query(Users).filter(Users.id == user_id, Users.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.points += points
    db.commit()
    db.refresh(user)
    return user


        
@auth_router.post("/forgot-password", status_code=status.HTTP_200_OK)
async def forgot_password(request: ForgotPasswordRequest, db: db_dependency):
    try:
        user = db.query(Users).filter(Users.email == request.email).first()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="No account found with this email address"
            )
        
        # Generate reset token
        reset_token = secrets.token_urlsafe(32)
        user.password_reset_token = reset_token
        user.password_reset_expires = datetime.now(timezone.utc) + timedelta(hours=1)
        
        # Save token to database
        db.commit()
        
        return {
            "status": "success",
            "message": "Password reset instructions sent",
            "token": user.password_reset_token
        }
        
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@auth_router.post("/reset-password")
async def reset_password(request: ResetPasswordRequest, db: db_dependency):
    try:
        user = db.query(Users).filter(Users.password_reset_token == request.token).first()
        
        if not user:
            raise HTTPException(
                status_code=404,
                detail="Invalid reset token"
            )
            
        current_time = datetime.now(timezone.utc)
        if user.password_reset_expires < current_time:
            raise HTTPException(
                status_code=400,
                detail="Reset token has expired"
            )
            
        # Update password
        user.hashed_password = bcrypt_context.hash(request.new_password)
        
        # Clear reset token
        user.password_reset_token = None
        user.password_reset_expires = None
        
        # Save changes
        db.commit()
        
        return {
            "status": "success",
            "message": "Password has been reset successfully"
        }
        
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


    
@user_router.get("/users", response_model=List[UserBase])
async def get_all_users(db: db_dependency):
    users = db.query(Users).all()  # Retrieve all users from the database
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

    


@user_router.put("/user/{user_id}/{email}/login_time")
async def update_user_login_time(user_id: int, email: str, db: db_dependency):
    user = db.query(Users).filter(Users.id == user_id, Users.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user.last_login is None:
        user.last_login = datetime.now(timezone.utc)
        user.points = 100
        print('Login time updated')
    elif user.last_login < datetime.now(timezone.utc) - timedelta(days=1):
        user.last_login = datetime.now(timezone.utc)
        user.points += 100
        print('Login time updated')
    else:
        print('Login time not updated')
    db.commit()
    db.refresh(user)
    return user



@user_router.put("/user/{user_id}", response_model=UserBase)
async def update_user(user_id: int, user_update: dict, db: db_dependency):
    try:
        print(f"Received update request for user {user_id}")
        print(f"Update fields: {list(user_update.keys())}")
        
        user = db.query(Users).filter(Users.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Handle profile image specifically
        if 'profile_image' in user_update:
            profile_image = user_update['profile_image']
            print(f"Received profile image: {'None' if profile_image is None else 'Length: ' + str(len(profile_image))}")
            
            # Check if it's a valid base64 string
            if profile_image and isinstance(profile_image, str):
                if not profile_image.startswith('data:image'):
                    raise HTTPException(status_code=400, detail="Invalid image format")
            user.profile_image = profile_image
            
        # Update other fields
        for key, value in user_update.items():
            if hasattr(user, key) and key != 'profile_image':
                setattr(user, key, value)
        
        user.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(user)
        print("User update successful")
        return user
    except Exception as e:
        print(f"Error updating user: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
@user_router.delete("/user/{user_id}", status_code=200)
async def delete_user(user_id: int, db: db_dependency):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return None

# @user_router.put("/user/{user_id}/subscription")
