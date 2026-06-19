# ==========================================
# Codeaura Industry Project: Backend (FastAPI)
# ==========================================
# Ye ek asli Server hai jo AI Chatbot ko chalayega aur Database se connect hoga.

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import datetime

# FastAPI app banana
app = FastAPI(title="Codeaura AI Assistant API")

# Model for incoming messages
class ChatMessage(BaseModel):
    user_text: str

# 1. Database Connection Logic (MongoDB Example)
# Real industry me hum 'motor' ya 'pymongo' use karte hain MongoDB se judne ke liye
def save_to_database(user_text, ai_reply):
    # This is a dummy function. In real life, it connects to AWS or MongoDB Atlas.
    print(f"[DB SAVE] Time: {datetime.datetime.now()} | User: {user_text} | AI: {ai_reply}")

# 2. AI Logic (Here we use a Dummy AI, students can replace it with OpenAI API)
def get_ai_response(text: str):
    text = text.lower()
    if "hello" in text or "hi" in text:
        return "Hello! Welcome to Codeaura. How can I help you today?"
    elif "course" in text:
        return "We offer courses in Python, AI, Web Development, and more!"
    elif "fees" in text:
        return "Please visit our website or contact support for fee details."
    else:
        return "I am an AI Assistant. I am still learning, but I will get a human to help you soon!"

# 3. API Route for the Chatbot
@app.post("/api/chat")
async def chat_endpoint(message: ChatMessage):
    # Step A: Get AI response
    reply = get_ai_response(message.user_text)
    
    # Step B: Save to Database
    save_to_database(message.user_text, reply)
    
    # Step C: Send response back to the Frontend UI
    return {"reply": reply}

# 4. Frontend Webpage Route
# Jab koi server ka link kholega, to use ye HTML dikhega
@app.get("/")
async def get_frontend():
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

# Run instructions for students:
# uvicorn main:app --reload
