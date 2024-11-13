from sqlalchemy.orm import Session
from .models import Users, DestinationData, ItineraryData
from .schemas import UserCreate, DestinationCreate, ItineraryCreate

# User CRUD operations

# Create a new user
def create_user(db: Session, user: UserCreate):
    new_user = Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get a user by ID
def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Users).offset(skip).limit(limit).all()

# Update a user's email
def update_user_email(db: Session, user_id: int, new_email: str):
    user = get_user(db, user_id)
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
        return user
    return None

# Delete a user by ID
def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

# Destination CRUD operations

# Create a new destination
def create_destination(db: Session, destination: DestinationCreate):
    new_destination = DestinationData(**destination.dict())
    db.add(new_destination)
    db.commit()
    db.refresh(new_destination)
    return new_destination

# Get a destination by ID
def get_destination(db: Session, destination_id: int):
    return db.query(DestinationData).filter(DestinationData.destination_id == destination_id).first()

# Get all destinations
def get_destinations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DestinationData).offset(skip).limit(limit).all()

# Update a destination's details
def update_destination(db: Session, destination_id: int, updated_data: dict):
    destination = get_destination(db, destination_id)
    if destination:
        for key, value in updated_data.items():
            setattr(destination, key, value)
        db.commit()
        db.refresh(destination)
        return destination
    return None

# Delete a destination by ID
def delete_destination(db: Session, destination_id: int):
    destination = get_destination(db, destination_id)
    if destination:
        db.delete(destination)
        db.commit()
        return True
    return False

# Itinerary CRUD operations

# Create a new itinerary
def create_itinerary(db: Session, itinerary: ItineraryCreate):
    new_itinerary = ItineraryData(**itinerary.dict())
    db.add(new_itinerary)
    db.commit()
    db.refresh(new_itinerary)
    return new_itinerary

# Get an itinerary by ID
def get_itinerary(db: Session, itinerary_id: int):
    return db.query(ItineraryData).filter(ItineraryData.itinerary_id == itinerary_id).first()

# Get all itineraries
def get_itineraries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ItineraryData).offset(skip).limit(limit).all()

# Update an itinerary's details
def update_itinerary(db: Session, itinerary_id: int, updated_data: dict):
    itinerary = get_itinerary(db, itinerary_id)
    if itinerary:
        for key, value in updated_data.items():
            setattr(itinerary, key, value)
        db.commit()
        db.refresh(itinerary)
        return itinerary
    return None

# Delete an itinerary by ID
def delete_itinerary(db: Session, itinerary_id: int):
    itinerary = get_itinerary(db, itinerary_id)
    if itinerary:
        db.delete(itinerary)
        db.commit()
        return True
    return False
