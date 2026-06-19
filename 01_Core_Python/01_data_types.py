# ==========================================
# Codeaura Python Course: 01_data_types.py
# ==========================================
# In this file, we will understand basic Python Data Types.

# 1. Integers (Whole numbers without decimals)
age = 22
print("Age:", age, "| Type:", type(age))

# 2. Floats (Numbers with decimals)
height = 5.8
print("Height:", height, "| Type:", type(height))

# 3. Strings (Text data)
name = "Codeaura Student"
print("Name:", name, "| Type:", type(name))

# 4. Booleans (True or False)
is_learning = True
print("Learning:", is_learning, "| Type:", type(is_learning))

# ==========================================
# ADVANCED DATA TYPES (Data Structures)
# ==========================================

# 5. Lists (Store multiple items in a single variable. These are mutable - can be changed)
skills = ["Python", "Data Science", "AI"]
skills.append("Machine Learning") # Adding a new item
print("\nSkills List:", skills)

# 6. Tuples (Similar to lists, but they are immutable - cannot be changed)
coordinates = (28.7041, 77.1025)
print("Coordinates Tuple:", coordinates)

# 7. Dictionaries (Store data in Key-Value pairs)
student_info = {
    "name": "Rohan",
    "course": "Data Analytics",
    "duration_months": 6
}
print("Student Dictionary:", student_info)
print("Student Name is:", student_info["name"])

# 8. Sets (Collection of unique items, does not allow duplicates)
unique_numbers = {1, 2, 2, 3, 4, 4, 5}
print("Unique Set:", unique_numbers) # Duplicates will be automatically removed in the output
