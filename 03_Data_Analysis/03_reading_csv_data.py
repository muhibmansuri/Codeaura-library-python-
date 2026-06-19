# ==========================================
# Codeaura Python Course: 03_reading_csv_data.py
# ==========================================
# In this file, we will learn how to read data from a real file (CSV).

import pandas as pd

print("--- 1. Reading a CSV File ---")
# 'pd.read_csv()' reads the data and converts it into a DataFrame (Table).
# Make sure 'students_data.csv' is in the same folder as this code!
try:
    df = pd.read_csv("students_data.csv")
    print("Data loaded successfully!\n")
    
    # Show the entire table
    print(df)
    
except FileNotFoundError:
    print("Error: The file 'students_data.csv' was not found. Please check the folder.")


print("\n--- 2. Checking the Data ---")
# If the table is very big, we can use head() to see only the first 5 rows
print("\nFirst 3 rows:")
print(df.head(3))

# Using info() tells us about the columns and if any data is missing
print("\nData Information:")
df.info()

# Note for Students: Run this file and look at the 'info()'. 
# It will tell you that some marks and ages are missing!
