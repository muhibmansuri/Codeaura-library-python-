# ==========================================
# Codeaura Python Course: 04_data_cleaning.py
# ==========================================
# In real life, data is often incomplete.
# In this file, we will learn how to clean messy data using Pandas.

import pandas as pd

# First, load the data again
df = pd.read_csv("students_data.csv")

print("--- Original Messy Data ---")
print(df)


print("\n--- 1. Finding Missing Data ---")
# isnull().sum() counts exactly how many boxes are empty in each column
print(df.isnull().sum())


print("\n--- 2. Cleaning Option A: Filling the Empty Boxes ---")
# If an age is missing, let's fill it with the average age (which is 21).
# If a mark is missing, let's fill it with a 0.

# Making a copy so we don't mess up the original table right away
cleaned_df_1 = df.copy()

# Fill missing Age with 21
cleaned_df_1["Age"] = cleaned_df_1["Age"].fillna(21)

# Fill missing Marks with 0
cleaned_df_1["Marks"] = cleaned_df_1["Marks"].fillna(0)

print("\nData after filling empty boxes:")
print(cleaned_df_1)


print("\n--- 3. Cleaning Option B: Deleting Incomplete Rows ---")
# Sometimes it's better to just delete any student who has missing data.
# dropna() removes any row that has an empty box (NaN).

cleaned_df_2 = df.dropna()

print("\nData after deleting incomplete rows:")
print(cleaned_df_2)

# Note for Students: Data Cleaning is the most important job of a Data Scientist!
