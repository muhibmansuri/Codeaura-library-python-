# ==========================================
# Codeaura Python Course: 03_mini_chatbot.py
# ==========================================
# Concept: Chatbots (Machine se baatein karna)
# Real Life Example: Ek chota sa Pizza Order karne wala Chatbot jo aapke text ko samajh kar reply dega.

import random

print("--- Codeaura Mini Pizza Chatbot ---")
print("Chatbot: Hello! I am the Pizza Bot. Type 'exit' to stop talking.\n")

# Chatbot ke pass kuch pehle se soche hue answers (responses) hain
greetings = ["hello", "hi", "hey"]
pizza_types = ["cheese", "pepperoni", "veg", "margarita"]

while True:
    # User se message lena
    user_input = input("You: ").lower() # lower() se sara text chote letters me ho jayega
    
    # Agar user ne 'exit' likha to baat band
    if user_input == "exit":
        print("Chatbot: Bye! Have a great day.")
        break
        
    # Machine ka logic: Wo words pakadne ki koshish karegi
    if any(word in user_input for word in greetings):
        print("Chatbot: Hi there! Would you like to order a pizza?")
    
    elif "order" in user_input or "pizza" in user_input:
        print(f"Chatbot: Great! We have {', '.join(pizza_types)}. Which one do you want?")
        
    elif any(pizza in user_input for pizza in pizza_types):
        print("Chatbot: Awesome choice! Your pizza will be ready in 15 minutes. 🍕")
        
    else:
        # Agar machine nahi samajh payi
        responses = ["I didn't understand that.", "Can you please say that again?", "I only talk about pizzas!"]
        print("Chatbot:", random.choice(responses))

# Note for Students: Ye bahut basic chatbot hai (if/else se chalta hai). 
# ChatGPT jaise advance chatbots Artificial Neural Networks se chalte hain!
