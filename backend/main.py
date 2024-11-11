"""
Main application entry point for FastAPI server setup and routing.
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from .crud import (
    create_user, get_user, get_users, update_user_email, delete_user,
    create_destination, get_destination, get_destinations, update_destination, delete_destination,
    create_itinerary, get_itinerary, get_itineraries, update_itinerary, delete_itinerary
)
from .schemas import UserCreate, UserResponse, DestinationCreate, DestinationResponse, ItineraryCreate, ItineraryResponse
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
def update_user_email_endpoint(user_id: int, new_email: str, db: Session = Depends(get_db)):
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

# Destination endpoints using the "Destination" tag
@app.post("/destination", response_model=DestinationResponse, tags=["Destination"])
def create_destination_endpoint(destination: DestinationCreate, db: Session = Depends(get_db)):
    """Create a new destination."""
    return create_destination(db, destination)

@app.get("/destinations", response_model=list[DestinationResponse], tags=["Destination"])
def get_destinations_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of destinations with pagination."""
    return get_destinations(db, skip=skip, limit=limit)

@app.get("/destination/{destination_id}", response_model=DestinationResponse, tags=["Destination"])
def get_destination_endpoint(destination_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific destination by ID."""
    destination = get_destination(db, destination_id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination

@app.put("/destination/{destination_id}", response_model=DestinationResponse, tags=["Destination"])
def update_destination_endpoint(destination_id: int, updated_data: dict, db: Session = Depends(get_db)):
    """Update the details of a specific destination by ID."""
    destination = update_destination(db, destination_id, updated_data)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination

@app.delete("/destination/{destination_id}", status_code=204, tags=["Destination"])
def delete_destination_endpoint(destination_id: int, db: Session = Depends(get_db)):
    """Delete a specific destination by ID."""
    if not delete_destination(db, destination_id):
        raise HTTPException(status_code=404, detail="Destination not found")
    return {"detail": "Destination deleted successfully"}

# Itinerary endpoints using the "Itinerary" tag
@app.post("/itinerary", response_model=ItineraryResponse, tags=["Itinerary"])
def create_itinerary_endpoint(itinerary: ItineraryCreate, db: Session = Depends(get_db)):
    """Create a new itinerary."""
    return create_itinerary(db, itinerary)

@app.get("/itineraries", response_model=list[ItineraryResponse], tags=["Itinerary"])
def get_itineraries_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of itineraries with pagination."""
    return get_itineraries(db, skip=skip, limit=limit)

@app.get("/itinerary/{itinerary_id}", response_model=ItineraryResponse, tags=["Itinerary"])
def get_itinerary_endpoint(itinerary_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific itinerary by ID."""
    itinerary = get_itinerary(db, itinerary_id)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return itinerary

@app.put("/itinerary/{itinerary_id}", response_model=ItineraryResponse, tags=["Itinerary"])
def update_itinerary_endpoint(itinerary_id: int, updated_data: dict, db: Session = Depends(get_db)):
    """Update the details of a specific itinerary by ID."""
    itinerary = update_itinerary(db, itinerary_id, updated_data)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return itinerary

@app.delete("/itinerary/{itinerary_id}", status_code=204, tags=["Itinerary"])
def delete_itinerary_endpoint(itinerary_id: int, db: Session = Depends(get_db)):
    """Delete a specific itinerary by ID."""
    if not delete_itinerary(db, itinerary_id):
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return {"detail": "Itinerary deleted successfully"}
