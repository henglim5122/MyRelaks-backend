from fastapi import APIRouter, Depends, Path, HTTPException
from database import SessionLocal
from typing import Annotated 
from sqlalchemy.orm import Session
from pydantic import BaseModel, StrictInt, Field
from typing import Optional
from .auth import get_current_user
from models import Destination,CustomerPreference

router = APIRouter(tags=["Destination"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class DestRequest(BaseModel):
    id: Optional[StrictInt] = None
    name: str
    location: str
    state: str
    coordinate: str
    description: str
    reviewRating: float
    activityCategory : str
    src: str
    openingHours: Optional[str] = None
    minPrice: Optional[float] = None
    maxPrice: Optional[float] = None
    liked_by: bool = False

class LikeDestRequest(BaseModel):
    user_id: int
    destination_id: int

@router.get("/destinations")
async def read_all(db: db_dependency):
    return db.query(Destination).all()


@router.get("/destinations/{destination_id}")
async def get_destination_by_id(db: db_dependency, destination_id: int = Path(gt=0)):
    destination_result = db.query(Destination).filter(Destination.id == destination_id).first()

    if destination_result is not None:
        return destination_result
    
    raise HTTPException(status_code=404, detail="Destination not found") 

@router.get("/liked_destinations/{user_id}")
async def get_liked_destination_by_user_id(db: db_dependency, user: user_dependency, user_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return db.query(CustomerPreference).filter(CustomerPreference.user_id == user_id).all()

@router.delete("/liked_destinations/{user_id}")
async def delete_destination_by_user_id(db: db_dependency, user: user_dependency, user_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    result = db.query(CustomerPreference).filter(CustomerPreference.user_id == user_id).all()
    if result is None:
        return {"message": "Destination List not found"}
    else:
        db.query(CustomerPreference).filter(CustomerPreference.user_id == user_id).delete()
        db.commit()
        # db.refresh()
        return {"message": "Destinations all removed successfully"}

    
@router.post("/liked_destinations")
async def create_like_destination(db: db_dependency, user: user_dependency, liked_destination: LikeDestRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    customer_preference = CustomerPreference(destination_id=liked_destination.destination_id, user_id=liked_destination.user_id)
    result = db.query(CustomerPreference).filter(CustomerPreference.user_id == liked_destination.user_id, CustomerPreference.destination_id == liked_destination.destination_id).first()
    if result is not None:
        return {"message": "Destination already liked"}     
    else:
        db.add(customer_preference)
    db.commit()
    # db.refresh(customer_preference)
    return {"message": "Destination liked successfully"}    

@router.delete("/liked_destinations/{user_id}/{destination_id}")
async def delete_destination(db: db_dependency, user: user_dependency, destination_id: int = Path(gt=0), user_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    result = db.query(CustomerPreference).filter(CustomerPreference.user_id == user_id, CustomerPreference.destination_id == destination_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Destination not found")
    else:
        db.query(CustomerPreference).filter(CustomerPreference.user_id == user_id, CustomerPreference.destination_id == destination_id).delete()
        db.commit()
        # db.refresh()
        return {"message": "Destination unliked successfully"}

@router.get("/destinationsuser")
async def read_all(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user







# @router.post("/destinations")
# async def create_destination(user: user_dependency, db: db_dependency, destination_request: DestRequest):
#     if user is None:
#         raise HTTPException(status_code=401, detail="Not authenticated")
    
#     destination = Destinations(**destination_request.model_dump())
#     db.add(destination)
#     db.commit()

# @router.put("/destinations/{destination_id}")
# async def update_destination(user: user_dependency,
#                       db: db_dependency,                        
#                       destination_request: DestRequest,
#                       destination_id: int = Path(gt=0)):
#     if user is None:
#         raise HTTPException(status_code=401, detail="Not authenticated")
    
#     destination_result = db.query(Destinations).filter(Destinations.id == destination_id).filter(Destinations.customer_id == user.get("id")).first()

#     if destination_result is None:
#         raise HTTPException(status_code=404, detail="Book not found")
    
#     destination_result.name = destination_request.name 
#     destination_result.location = destination_request.location
#     destination_result.state = destination_request.state
#     destination_result.coordinate = destination_request.coordinate
#     destination_result.description = destination_request.description
#     destination_result.reviewRating = destination_request.reviewRating
#     destination_result.activityCategory = destination_request.activityCategory
#     destination_result.src = destination_request.src
#     destination_result.openingHours = destination_request.openingHours
#     destination_result.minPrice = destination_request.minPrice
#     destination_result.maxPrice = destination_request.maxPrice

    
#     db.add(destination_result)
#     db.commit()

# @router.delete("/books/{book_id}")
# async def delete_book(user: user_dependency, db: db_dependency, book_id: int = Path(gt=0)):
#     if user is None:
#         raise HTTPException(status_code=401, detail="Not authenticated")
    
#     book_result = db.query(Books).filter(Books.id == book_id).filter(Books.customer_id == user.get("id")).first()

#     if book_result is None:
#         raise HTTPException(status_code=404, detail="Book not found")
#     else:
#         db.query(Books).filter(Books.id == book_id).delete()
    
#     db.commit()
    