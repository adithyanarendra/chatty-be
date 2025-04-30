from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.schemas import ChatRequest, ChatResponse
from app.models.db import SessionLocal
from app.services.chat_logic import get_bot_response

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    user_message = request.message
    bot_reply = get_bot_response(user_message, db)
    return ChatResponse(reply=bot_reply)


@router.post("/retrain")
async def retrain():
    from app.retrain_model import retrain_model
    retrain_model()
    return {"message": "Model retrained successfully"}
