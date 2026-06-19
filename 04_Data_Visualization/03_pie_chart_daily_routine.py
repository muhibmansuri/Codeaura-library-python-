# ==========================================
# Codeaura Python Course: 03_pie_chart_daily_routine.py
# ==========================================
# Concept: Pie Chart (Gol pizza jaisa graph)
# Ye tab use hota hai jab hume dikhana ho ki ek puri cheez (100%) me se kiska kitna hissa (slice) hai.
# Real Life Example: Ek student ka 24 ghante ka routine.

import matplotlib.pyplot as plt

# Ek din me 24 ghante hote hain. Humne use 4 hisso me baant diya hai.
activities = ["Sleep", "Study", "Play/Gym", "Other (Eating, TV)"]
hours = [8, 6, 3, 7] # Total = 24

# Slices ke colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

print("Creating Daily Routine Pie Chart...")

# plt.pie() se gol graph banta hai
# autopct='%1.1f%%' se har slice ke andar percentage (%) likha aayega
# explode=(0.1, 0, 0, 0) se pehla slice (Sleep) thoda bahar nikal kar dikhega
plt.pie(hours, labels=activities, colors=colors, autopct='%1.1f%%', explode=(0.1, 0, 0, 0), shadow=True, startangle=140)

# Graph ko Title dena
plt.title("A Student's 24-Hour Daily Routine")

# Graph ko screen par dikhana
plt.show()

print("Pie chart displayed! Notice how the 'Sleep' slice is slightly pulled out for emphasis.")
