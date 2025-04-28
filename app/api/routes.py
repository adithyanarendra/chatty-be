from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat_logic import get_bot_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_message = request.message
    bot_reply = get_bot_response(user_message)
    return ChatResponse(reply=bot_reply)
