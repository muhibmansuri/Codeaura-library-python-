# ==========================================
# Codeaura Python Course: 02_first_neural_network.py
# ==========================================
# Concept: Creating a basic Neural Network
# Real Life Example: Ek aisi machine banana jo Celsius ko Fahrenheit me convert karna khud seekhegi!
# Hum use koi formula (F = C * 1.8 + 32) nahi batayenge, wo data dekh kar khud formula banayegi.

import tensorflow as tf
import numpy as np

print("--- Our First Artificial Brain (Neural Network) ---")

# Step 1: Humara Data (Kuch Temperatures)
# Celsius values (Question)
celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
# Fahrenheit values (Answer)
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

print("\nStep 1: Giving data to the brain...")

# Step 2: Dimaag ka Structure Banana (Neural Network Layout)
# 'Dense' ka matlab hai ek layer jisme Neurons (dimaag ke cells) hain.
# Yahan hum bas ek simple Neuron le rahe hain (units=1).
layer_0 = tf.keras.layers.Dense(units=1, input_shape=[1])

# Is layer ko ek 'Sequential' model (dimag) me dalna
model = tf.keras.Sequential([layer_0])

# Dimaag ko set karna: 
# loss = Galti ko naapna (Mean Squared Error)
# optimizer = Galti ko theek karna (Adam optimizer)
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

# Step 3: Dimaag ko sikhana (Training)
# 'epochs=500' matlab machine 500 baar padhai karegi!
print("Step 2: Training the brain (This might take a few seconds)...")
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Training Complete! The brain has learned the rule.")

# Step 4: Machine se naya sawaal puchna (Prediction)
# Agar temperature 100 Celsius hai, to Fahrenheit kya hoga? (Hume pata hai 212 hona chahiye)
new_temp = np.array([100.0])
predicted_answer = model.predict(new_temp)

print(f"\nResult: Agar bahar 100 degrees Celsius hai,")
print(f"To hamare Artificial Brain ke hisaab se Fahrenheit me wo lagbhag {int(predicted_answer[0][0])} F hoga!")
print("(Exact formula F = C * 1.8 + 32 se ye 212 hota hai, machine bina formula ke iske kitna kareeb aa gayi!)")
