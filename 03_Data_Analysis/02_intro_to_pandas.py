# ==========================================
# Codeaura Python Course: 02_intro_to_pandas.py
# ==========================================
# In this file, we will learn Pandas.
# Pandas is used to work with data that looks like tables (like Excel).

import pandas as pd

print("--- 1. Pandas Series (A Single Column) ---")
# A Series is just a single column of data.
ages = pd.Series([21, 22, 20, 23], name="Student_Ages")
print(ages)


print("\n--- 2. Pandas DataFrame (A Complete Table) ---")
# A DataFrame is a complete table with rows and columns.
# Let's create a dictionary of data first:
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [21, 22, 20, 23],
    "Course": ["Python", "Data Science", "AI", "Python"]
}

# Now convert the dictionary into a DataFrame (Table)
df = pd.DataFrame(data)

print("Our Student Table:\n")
print(df)


print("\n--- 3. Accessing Data ---")
# Get only the Names column
print("\nOnly Names:")
print(df["Name"])

# Note for Students: A DataFrame makes Python look exactly like an Excel sheet!
