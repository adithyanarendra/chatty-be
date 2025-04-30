from pydantic import BaseModel
from datetime import datetime


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


class ChatHistoryBase(BaseModel):
    message: str
    predicted_intent: str
    timestamp: datetime

    class Config:
        from_attributes = True


class ChatHistoryCreate(ChatHistoryBase):
    pass


class ChatHistory(ChatHistoryBase):
    id: int
