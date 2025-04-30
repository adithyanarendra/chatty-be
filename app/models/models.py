from sqlalchemy import Column, Integer, String, DateTime
from app.models.db import Base
from datetime import datetime


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    predicted_intent = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
