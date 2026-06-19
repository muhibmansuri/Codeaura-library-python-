# ==========================================
# Codeaura Python Course: 01_fastapi_server.py
# ==========================================
# Concept: Backend APIs (FastAPI)
# Real Life Example: Swiggy ya Zomato ka server. 
# Jab aap mobile se Pizza order karte hain, to apka message ek "API" ke jariye Server tak jata hai, 
# aur server jawab (response) deta hai ki "Order Accepted".

from fastapi import FastAPI

print("--- Starting Codeaura Backend Server ---")

# Step 1: Ek naya Server/API banana
app = FastAPI()

# Step 2: Server ka ek 'Route' (Address) set karna
# Jab koi server ke home page ('/') par aayega, to kya jawab dena hai?
@app.get("/")
def home():
    return {"message": "Welcome to Codeaura API! The server is running perfectly."}

# Step 3: Swiggy wala example (Ek Pizza Order karne ka API)
@app.get("/order_pizza/{pizza_name}")
def order_food(pizza_name: str):
    return {
        "status": "Success",
        "message": f"Your order for {pizza_name} Pizza has been received!",
        "delivery_time": "30 mins"
    }

# Note for Students:
# Ise chalane ke liye Terminal me likhein:
# uvicorn 01_fastapi_server:app --reload
# Fir apne browser me (http://127.0.0.1:8000/order_pizza/cheese) khol kar dekhein, magic dikhega!
