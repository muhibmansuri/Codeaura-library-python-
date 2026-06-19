# ==========================================
# Codeaura Python Course: 01_streamlit_website.py
# ==========================================
# Concept: Web Frontend in Python (Streamlit)
# Real Life Example: Sirf 5 line ka Python code likh kar asli, chalne wali Website banana!
# HTML, CSS, Javascript sikhne ki koi zaroorat nahi.

import streamlit as st

# Step 1: Website ka Title
st.title("Welcome to Codeaura's First Website! 🚀")

# Step 2: Website me Text dalna
st.write("Ye website sirf Python se banayi gayi hai. Koi HTML use nahi hua!")

# Step 3: Ek Button banana aur uspar click karne ka magic!
if st.button("Click Me for Magic"):
    st.balloons() # Website par gubbare udayega!
    st.success("Congratulations! Aapne apna pehla Web App bana liya hai.")

# Note for Students:
# Is file ko normal 'python 01_streamlit_website.py' ki tarah run nahi karna.
# Ise chalane ke liye Terminal me likhein:
# streamlit run 01_streamlit_website.py
