# ==========================================
# Codeaura Python Course: 03_classification_pass_fail.py
# ==========================================
# Concept: Classification (Predicting a Category: Yes/No, Pass/Fail)
# Real Life Example: Student ke padhne ke ghante dekh kar andaza lagana ki wo Pass hoga ya Fail.

from sklearn.tree import DecisionTreeClassifier
import numpy as np

print("--- Student Exam Predictor (Machine Learning) ---")

# Step 1: Humara Purana Data (Training Data)
# Students ne din me kitne ghante padhai ki
study_hours = np.array([[1], [2], [3], [5], [6], [8]])

# Result: 0 matlab Fail, 1 matlab Pass
exam_results = np.array([0, 0, 0, 1, 1, 1])

print("\nStep 1: Machine is looking at past students' data...")

# Step 2: Machine Learning Model banana (Decision Tree is very simple and smart)
model = DecisionTreeClassifier()

# Step 3: Model ko sikhana (Training)
model.fit(study_hours, exam_results)
print("Step 2: Machine has learned the pattern (More hours = Pass)!")

# Step 4: Naye student ka result predict karna
new_student_hours = np.array([[4]]) # Ek naya student jo din me 4 ghante padhta hai
prediction = model.predict(new_student_hours)

print(f"\nResult: Naya student din me {new_student_hours[0][0]} ghante padhta hai.")
if prediction[0] == 1:
    print("Machine Prediction: Ye student aaram se PASS ho jayega! 🎉")
else:
    print("Machine Prediction: Ye student FAIL ho sakta hai, aur mehnat karni padegi! 📚")

# Note for Students: Try changing 'new_student_hours' to 7 or 1 and run the code again!
