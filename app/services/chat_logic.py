import os
from sqlalchemy.orm import Session
from sklearn.feature_extraction.text import TfidfVectorizer
from app.models import schemas, crud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from datetime import datetime
import joblib

vectorizer = TfidfVectorizer()
model = LogisticRegression()


def load_model():
    global model, vectorizer
    if os.path.exists("model.pkl") and os.path.exists("vectorizer.pkl"):
        model = joblib.load("model.pkl")
        vectorizer = joblib.load("vectorizer.pkl")
    else:
        print("Model files not found. Initializing with dummy model")
        from sklearn.dummy import DummyClassifier
        model = DummyClassifier(strategy="most_frequent")
        vectorizer = TfidfVectorizer()
        vectorizer.fit(["hello", "bye", "time", "weather", "unknown"])
        model.fit(vectorizer.transform(["hello", "bye", "time", "weather", "unknown"]),
                  ["greeting", "goodbye", "ask_time", "ask_weather", "fallback"])


def get_bot_response(user_message: str, db: Session) -> str:
    user_message = user_message.lower()

    X_test = vectorizer.transform([user_message])
    predicted_intent = model.predict(X_test)[0]

    chat_entry = schemas.ChatHistoryCreate(
        message=user_message,
        predicted_intent=predicted_intent,
        timestamp=datetime.utcnow()
    )
    crud.create_chat_history(db, chat_entry)

    if predicted_intent == "greeting":
        return "Hello! How can I assist you today? :)"
    elif predicted_intent == "goodbye":
        return "Goodbye! Have a wonderful rest of the day!"
    elif predicted_intent == "ask_time":
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"
    elif predicted_intent == "ask_weather":
        return "I am not connected to live weather yet, but I hope it's sunny!"
    else:
        return "I'm sorry, I didn't understand that."
