# ==========================================
# Codeaura Python Course: 02_linear_regression_house_prices.py
# ==========================================
# Concept: Linear Regression (Predicting a continuous number)
# Real Life Example: Ghar ka size dekh kar uski Price (keemat) ka andaza lagana.

from sklearn.linear_model import LinearRegression
import numpy as np

print("--- House Price Predictor (Machine Learning) ---")

# Step 1: Humara Purana Data (Training Data)
# Ghar ka size (Square Feet me)
house_sizes = np.array([[800], [1000], [1500], [2000], [2500]])

# Ghar ki Price (Lakh Rupees me)
house_prices = np.array([30, 40, 60, 80, 100])

print("\nStep 1: Machine ko purana data diya ja raha hai...")

# Step 2: Machine Learning Model banana
model = LinearRegression()

# Step 3: Model ko sikhana (Training)
# 'fit' ka matlab hai model ko data se sikhana
model.fit(house_sizes, house_prices)
print("Step 2: Machine ne data se pattern seekh liya hai!")

# Step 4: Naye ghar ki price ka andaza lagana (Prediction)
new_house_size = np.array([[1200]]) # Ek naya ghar jo 1200 sq ft ka hai
predicted_price = model.predict(new_house_size)

print(f"\nResult: Agar ghar {new_house_size[0][0]} Square Feet ka hai,")
print(f"To Machine ke hisaab se uski price lagbhag {int(predicted_price[0])} Lakh Rupees hogi!")

# Note for Students: Machine ne khud calculate kiya ki har sq ft ka kitna rate chal raha hai!
