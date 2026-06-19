# ==========================================
# Codeaura Python Course: 05_oop_basics.py
# ==========================================
# In this file, we will learn Object-Oriented Programming (OOP).
# OOP is a way of writing code by thinking about real-world objects.

# Real-world Example: 
# Think of a 'Class' as an architectural blueprint (naksha) of a house.
# Think of an 'Object' as the actual physical house built using that blueprint.

# ---------------------------------------------------------
# Step 1: Creating a Class (The Blueprint)
# ---------------------------------------------------------
class Student:
    
    # This is a special function called the "constructor".
    # It automatically runs whenever we create a new student object.
    # 'self' refers to the specific student we are creating.
    def __init__(self, name, age, course):
        self.name = name       # Setting the student's name
        self.age = age         # Setting the student's age
        self.course = course   # Setting the student's course

    # This is a custom function (method) that belongs to the student
    def show_details(self):
        print("--- Student ID Card ---")
        print(f"Name:   {self.name}")
        print(f"Age:    {self.age}")
        print(f"Course: {self.course}")
        print("-----------------------")

    def study(self):
        print(f"{self.name} is currently studying {self.course}...")


# ---------------------------------------------------------
# Step 2: Creating Objects (The Actual Students)
# ---------------------------------------------------------
print("Creating new student records...\n")

# Student 1
student1 = Student("Rahul Sharma", 22, "Machine Learning")

# Student 2
student2 = Student("Priya Patel", 21, "Data Analytics")


# ---------------------------------------------------------
# Step 3: Using the Objects
# ---------------------------------------------------------
# Now we can ask student1 to show their details
student1.show_details()

# Ask student2 to show their details
student2.show_details()

# Calling the study action
print("\nActivities:")
student1.study()
student2.study()

# Note for Students: 
# Try creating a 'student3' object with your own name and course, 
# and then call student3.show_details()!
