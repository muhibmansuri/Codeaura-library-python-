# ==========================================
# Codeaura Python Course: 04_file_handling.py
# ==========================================
# In this file, we will learn how to read and write files in Python.
# Think of it like opening a Notepad file, typing something, and saving it, 
# but we are doing it using Python code!

# ---------------------------------------------------------
# Step 1: Writing data to a new file
# ---------------------------------------------------------
# We use the open() function. 
# "w" means "write mode". If the file does not exist, Python creates it.
print("--- Creating a new file ---")

# Let's create a file to store a student's marks
file = open("student_marks.txt", "w")
file.write("Name: Rahul Sharma\n")
file.write("Course: Data Science\n")
file.write("Score: 95/100\n")
file.close() # Always remember to close the file after you finish!
print("Success: 'student_marks.txt' has been created and saved.\n")


# ---------------------------------------------------------
# Step 2: Reading data from an existing file
# ---------------------------------------------------------
# "r" means "read mode". It reads what is already written inside the file.
print("--- Reading from the file ---")

file = open("student_marks.txt", "r")
content = file.read() # Read the entire text
print(content)
file.close()


# ---------------------------------------------------------
# Step 3: The Best Way to Handle Files (Using 'with')
# ---------------------------------------------------------
# Using 'with' is a professional way because it automatically closes the file for you.
# You don't have to write file.close() manually!
print("--- Appending (adding) new data using 'with' ---")

# "a" means "append mode". It adds new text to the end without deleting the old text.
with open("student_marks.txt", "a") as file:
    file.write("Status: Passed with A+ Grade\n")

print("New line added! Let's read the final file:\n")

# Reading it again using 'with'
with open("student_marks.txt", "r") as file:
    print(file.read())

print("Note for Students: Try changing the name 'Rahul' to your own name and run the code!")
