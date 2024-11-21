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