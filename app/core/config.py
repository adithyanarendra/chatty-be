import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://chatuser:chatpass@localhost:5432/chatbot_db")
