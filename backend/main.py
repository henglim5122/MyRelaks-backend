"""
Main application entry point for FastAPI server setup and routing.
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from routes.auth import auth_router
from schemas import UserCreate, UserResponse
from crud import create_user, get_user, get_users, update_user_email, delete_user

app = FastAPI(debug=True)

# CORS settings
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Include the auth router
app.include_router(auth_router)

# Create a new user
@app.post("/users/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new user.
    """
    return create_user(db, user)


# Get a user by ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user by their ID.
    """
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Get all users
@app.get("/users/", response_model=list[UserResponse])
def get_users_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of users with pagination.
    """
    return get_users(db, skip=skip, limit=limit)


# Update a user's email
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user_email_endpoint(
    user_id: int, new_email: str, db: Session = Depends(get_db)
):
    """
    Update the email of a user by their ID.
    """
    user = update_user_email(db, user_id, new_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Delete a user
@app.delete("/users/{user_id}", status_code=204)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by their ID.
    """
    if not delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
