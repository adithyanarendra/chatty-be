from fastapi import FastAPI
from app.api.routes import router
from app.services.chat_logic import load_model
from app.models.db import Base, engine
from app.models import models

app = FastAPI()


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

load_model()

app.include_router(router)
