from sqlalchemy.orm import Session
from app.models import schemas
from app.models.db import SessionLocal
from app.models import models

# Add a chat to the history


def create_chat_history(db: Session, chat: schemas.ChatHistoryCreate):
    db_chat = models.ChatHistory(
        message=chat.message,
        predicted_intent=chat.predicted_intent,
        timestamp=chat.timestamp,
    )
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

# Get all chat history


def get_chat_history(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ChatHistory).offset(skip).limit(limit).all()
