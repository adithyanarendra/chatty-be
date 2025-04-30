import joblib
from sqlalchemy.orm import Session
from app.models.db import SessionLocal
from app.models import crud, schemas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def retrain_model():
    db = SessionLocal()

    chats = crud.get_chat_history(db)
    messages = [chat.message for chat in chats]
    intents = [chat.predicted_intent for chat in chats]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(messages)

    model = LogisticRegression()
    model.fit(X, intents)

    joblib.dump(model, "model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

    print("Model retrained successfully!")


if __name__ == "__main__":
    retrain_model()
