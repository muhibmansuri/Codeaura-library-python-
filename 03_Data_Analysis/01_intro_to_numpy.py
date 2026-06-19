# ==========================================
# Codeaura Python Course: 01_intro_to_numpy.py
# ==========================================
# In this file, we will learn about NumPy (Numerical Python).
# NumPy is used to do math and calculations very fast!

# First, we need to import (bring in) the numpy library.
# We usually call it "np" for short.
import numpy as np

print("--- 1. Creating a NumPy Array ---")
# An array is like a list, but much faster for math.
student_marks = np.array([85, 90, 78, 92, 88])
print("Marks Array:", student_marks)
print("Data Type:", type(student_marks))


print("\n--- 2. Why NumPy is better than normal Lists ---")
# Imagine we want to give 5 bonus marks to every student.
# With normal lists, we would have to use a 'for loop'.
# With NumPy, we can just do this:
bonus_marks = student_marks + 5
print("Marks after 5 bonus points:", bonus_marks)


print("\n--- 3. Basic Calculations ---")
print("Highest Marks: ", np.max(student_marks))
print("Lowest Marks:  ", np.min(student_marks))
print("Average Marks: ", np.mean(student_marks))

print("\nNote for Students: Try changing the marks in the array and see how the average changes!")
