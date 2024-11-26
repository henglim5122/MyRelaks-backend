from fastapi import APIRouter, Depends, Path, HTTPException
from database import SessionLocal
from typing import Annotated 
from sqlalchemy.orm import Session
from pydantic import BaseModel, StrictInt, Field
from typing import Optional
from .auth import get_current_user
from models import Payment
from datetime import datetime, timezone

router = APIRouter(tags=["Destination"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class PaymentRequest(BaseModel):
    user_id: int
    aspect: str
    payment_method: str
    unique_id: str
    payment_amount: float
    payment_date: Optional[datetime] = None

@router.post("/payment")
async def create_payment(payment: PaymentRequest, db: db_dependency):
    try:
        payment_info = Payment(
            user_id=payment.user_id,
            aspect=payment.aspect,
            payment_method=payment.payment_method,
            unique_id=payment.unique_id,
            payment_date=datetime.now(timezone.utc),
            payment_amount=payment.payment_amount,
        )
        print(payment_info)
        db.add(payment_info)
        db.commit()
        
        return {"message": "Payment created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/payment/{user_id}")
async def get_payment_by_user_id(user_id: int, db: db_dependency):
    payment = db.query(Payment).filter(Payment.user_id == user_id).all()
    return payment

