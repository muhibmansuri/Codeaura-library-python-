# ==========================================
# Codeaura Python Course: 01_mongodb_concepts_dictionary.py
# ==========================================
# Concept: NoSQL Databases (Document Database like MongoDB)
# Real Life Example: NoSQL database me koi strict table nahi hoti. 
# Ye bilkul Python ki "Dictionary" (JSON) ki tarah data save karta hai. 
# Agar kisi student ka Roll Number nahi hai, tab bhi data save ho jayega. No rules!

print("--- NoSQL Database Concept (MongoDB Style) ---")

# MongoDB bilkul in Dictionaries jaisa dikhta hai:
student_1 = {
    "name": "Rahul Sharma",
    "age": 21,
    "course": "Python"
}

# Dekhiye! Dusre student me 'age' nahi hai, lekin 'skills' add ho gaya.
# SQL me ye karna bahut mushkil hai, par NoSQL me ye aaram se ho jata hai!
student_2 = {
    "name": "Priya Patel",
    "skills": ["C++", "Java", "Python"],
    "is_graduated": True
}

# NoSQL database (Collection) bas in dictionaries ka ek group hota hai:
nosql_database = [student_1, student_2]

print("\nData saved in NoSQL style:\n")
for document in nosql_database:
    print(document)

print("\nWhy use NoSQL?")
print("1. Flexible: Koi strict table nahi hai.")
print("2. Fast: Badi social media apps (like Instagram) iska use karti hain kyunki data format badalta rehta hai.")

# Note for Students: Asli MongoDB use karne ke liye hume 'pymongo' library install karni padti hai. Ye sirf ek aasan example tha!
