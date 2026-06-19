# ==========================================
# Codeaura Python Course: 02_amazon_review_checker.py
# ==========================================
# Concept: Sentiment Analysis (Jazbaat pehchanna)
# Real Life Example: Amazon par lakho reviews aate hain. Machine padh kar batayegi ki review Positive (Khush) hai ya Negative (Naraz).

from textblob import TextBlob

print("--- Amazon Product Review AI Checker ---")

# Hum machine ko 2 reviews denge
review_1 = "I love this laptop! It is extremely fast and the screen is beautiful."
review_2 = "This mobile is very bad. The battery drains too fast and the camera is terrible."

print(f"\nReview 1: '{review_1}'")
# TextBlob sentence ko padh kar uski 'polarity' nikalta hai. 
# Polarity -1 (Gussa) se +1 (Bahut Khush) tak hoti hai.
blob_1 = TextBlob(review_1)

if blob_1.sentiment.polarity > 0:
    print("Machine AI says: This is a POSITIVE review! 😃")
else:
    print("Machine AI says: This is a NEGATIVE review! 😡")


print(f"\nReview 2: '{review_2}'")
blob_2 = TextBlob(review_2)

if blob_2.sentiment.polarity > 0:
    print("Machine AI says: This is a POSITIVE review! 😃")
else:
    print("Machine AI says: This is a NEGATIVE review! 😡")

# Note for Students: Aap 'review_1' ki jagah apna khud ka english sentence likh kar try karein!
