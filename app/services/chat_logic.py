from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from datetime import datetime

# 1. Training examples
training_sentences = [
    "Hi", "Hello", "Hey there", "Good morning",
    "Bye", "Goodbye", "See you later", "Catch you later",
    "What time is it?", "Tell me the current time",
    "What's the weather?", "Is it going to rain today?"
]
training_intents = [
    "greeting", "greeting", "greeting", "greeting",
    "goodbye", "goodbye", "goodbye", "goodbye",
    "ask_time", "ask_time",
    "ask_weather", "ask_weather"
]

# 2. Vectorizer + Model setup
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_sentences)
model = LogisticRegression()
model.fit(X, training_intents)


def get_bot_response(user_message: str) -> str:
    user_message = user_message.lower()
    X_test = vectorizer.transform([user_message])
    predicted_intent = model.predict(X_test)[0]
    
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
