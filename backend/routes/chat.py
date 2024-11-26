from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import ChatHistory

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Message(BaseModel):
    sender: str
    text: str

class ChatSession(BaseModel):
    title: str
    messages: List[Message]
    timestamp: str
    user_id: Optional[str] = None

class ChatSessionInDB(ChatSession):
    id: str

router = APIRouter(tags=["Chat"])

@router.post("/save_chat")
async def save_chat(
    chat_session: ChatSession,
    db: Session = Depends(get_db)
):
    try:
        new_chat = ChatHistory(
            user_id=chat_session.user_id,
            title=chat_session.title,
            messages={"messages": [msg.dict() for msg in chat_session.messages]},
            timestamp=datetime.now()
        )
        db.add(new_chat)
        db.commit()
        db.refresh(new_chat)
        return {"message": "Chat saved successfully", "id": new_chat.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_chat_history/{user_id}")
async def get_chat_history(
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        chats = db.query(ChatHistory)\
            .filter(ChatHistory.user_id == user_id)\
            .order_by(ChatHistory.timestamp.desc())\
            .all()
        
        return [
            {
                "id": chat.id,
                "title": chat.title,
                "messages": chat.messages["messages"],
                "timestamp": chat.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
            for chat in chats
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

