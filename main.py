from fastapi import FastAPI
from chatbot import get_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Study Bot Running ✅"}

@app.post("/chat")
def chat(message: str):
    response = get_response(message)
    return {"reply": response}