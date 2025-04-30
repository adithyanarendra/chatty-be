from fastapi import FastAPI
from app.api.routes import router
from app.services.chat_logic import load_model

app = FastAPI()

load_model()

app.include_router(router)
