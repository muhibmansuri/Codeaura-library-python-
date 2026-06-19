# ==========================================
# Codeaura Python Course: 03_functions.py
# ==========================================
# In this file, we will learn how to create Functions.
# Functions are used to avoid writing the same code multiple times.

# 1. Simple Function
def greet_student():
    print("Welcome to Codeaura Institute!")

# Calling (executing) the function
greet_student()

# 2. Function with Parameters (Passing arguments)
def wish_student(name):
    print(f"Hello {name}, keep learning!")

wish_student("Rahul")
wish_student("Priya")

# 3. Function with Return Value (Returning a calculated result)
def calculate_percentage(obtained_marks, total_marks):
    percentage = (obtained_marks / total_marks) * 100
    return percentage

# Saving the result in a variable
rahul_score = calculate_percentage(400, 500)
print(f"Rahul's percentage: {rahul_score}%")

# 4. Lambda Function (A small, one-line function)
# Syntax: lambda arguments: expression
square = lambda x: x * x
print("Square of 5 is:", square(5))
