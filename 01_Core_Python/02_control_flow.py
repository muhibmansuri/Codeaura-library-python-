# ==========================================
# Codeaura Python Course: 02_control_flow.py
# ==========================================
# In this file, we will learn about Conditions and Loops.

print("--- IF/ELSE CONDITIONS ---")
marks = 85

# If marks are 80 or above, Grade A, else Grade B
if marks >= 80:
    print("Congratulations! You got Grade A.")
elif marks >= 60:
    print("You got Grade B.")
else:
    print("You need to work harder.")


print("\n--- FOR LOOPS ---")
# For loops are used to iterate over a sequence (like a list, tuple, or string).
topics = ["Python", "Pandas", "Machine Learning"]
for topic in topics:
    print("Today we will learn:", topic)

# Using range to print numbers (from 1 to 5)
for i in range(1, 6):
    print("Count:", i)


print("\n--- WHILE LOOPS ---")
# While loops execute as long as the condition remains True.
energy = 3
while energy > 0:
    print("Student is studying... Energy level:", energy)
    energy -= 1 # Decrease energy by 1
print("Energy depleted! Time to rest.")
