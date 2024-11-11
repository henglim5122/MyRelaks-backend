"""
Main application entry point for FastAPI server setup and routing.
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from .crud import create_user, get_user, get_users, update_user_email, delete_user
from .schemas import UserCreate, UserResponse
from .routes.auth import router as auth_router

# Initialize FastAPI application
app = FastAPI(debug=True)

# CORS settings
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine, checkfirst=True)

# Include the authentication router with the "Authorization" tag
app.include_router(auth_router, tags=["Authorization"])

# User endpoints using the "User" tag
@app.get("/user", response_model=UserResponse, tags=["User"])
async def get_current_user(db: Session = Depends(get_db)):
    """Get the current authenticated user."""
    user = db.query(models.Users).filter(models.Users.is_active).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users", response_model=list[UserResponse], tags=["User"])
def get_users_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of users with pagination."""
    return get_users(db, skip=skip, limit=limit)

@app.get("/user/{user_id}", response_model=UserResponse, tags=["User"])
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific user by ID."""
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/user/{user_id}", response_model=UserResponse, tags=["User"])
def update_user_email_endpoint(
    user_id: int, new_email: str, db: Session = Depends(get_db)
):
    """Update the email of a specific user by ID."""
    user = update_user_email(db, user_id, new_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/user/{user_id}", status_code=204, tags=["User"])
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """Delete a specific user by ID."""
    if not delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
