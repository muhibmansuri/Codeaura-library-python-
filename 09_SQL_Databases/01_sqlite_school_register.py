# ==========================================
# Codeaura Python Course: 01_sqlite_school_register.py
# ==========================================
# Concept: SQL Databases (Relational Database)
# Real Life Example: Ek digital School Register jisme data strictly tables (Rows and Columns) me save hota hai.
# Hum 'sqlite3' use karenge jo Python ke andar pehle se hota hai. Iske liye alag se server nahi chahiye!

import sqlite3

print("--- SQL Database: Digital School Register ---")

# Step 1: Database se connect karna (Agar nahi hai to automatically naya ban jayega)
conn = sqlite3.connect('school_data.db')
cursor = conn.cursor()

# Step 2: Ek Table (Register) banana
# ID: Roll number, Name: Student ka naam, Grade: Pass ya Fail
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Grade TEXT
    )
''')
print("Step 1: 'Students' naam ki table (Register) database me ban chuki hai.")

# Step 3: Table me Data (Bachho ka record) dalna
# Pehle purana data clear kar dete hain taki baar baar same data add na ho
cursor.execute('DELETE FROM Students')

cursor.execute("INSERT INTO Students (ID, Name, Grade) VALUES (1, 'Rahul Sharma', 'A')")
cursor.execute("INSERT INTO Students (ID, Name, Grade) VALUES (2, 'Priya Patel', 'B+')")
cursor.execute("INSERT INTO Students (ID, Name, Grade) VALUES (3, 'Amit Kumar', 'A+')")

# Data ko pakka save (commit) karna
conn.commit()
print("Step 2: 3 students ka record register me save ho gaya hai.\n")

# Step 4: Data ko Wapas Padhna (SELECT Query)
print("Step 3: Database se data padh rahe hain:")
print("-" * 30)
cursor.execute("SELECT * FROM Students")
all_students = cursor.fetchall()

for student in all_students:
    print(f"Roll No: {student[0]} | Name: {student[1]} | Grade: {student[2]}")
print("-" * 30)

# Step 5: Connection band karna (Good practice)
conn.close()

# Note for Students: Jab aap ye run karenge, to folder me 'school_data.db' naam ki ek nayi file ban jayegi. Wahi aapka asli database hai!
