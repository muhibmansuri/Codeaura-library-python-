# ==========================================
# Codeaura Python Course: 02_bar_chart_pocket_money.py
# ==========================================
# Concept: Bar Chart (Dando wala graph)
# Bar chart tab use hota hai jab hume alag-alag logo ya cheezon ko compare karna ho.
# Real Life Example: 4 Dosto ki Pocket Money ka comparison. Jiska danda lamba, uski pocket money zyada!

import matplotlib.pyplot as plt

# Dosto ke naam (Categories)
friends = ["Rahul", "Amit", "Priya", "Sneha"]

# Har ek ki pocket money (Values)
pocket_money = [1500, 2200, 1800, 3000]

print("Creating Pocket Money Bar Chart...")

# plt.bar() se dande wala graph banta hai
# Humne colors ki ek list di hai taki har dost ka danda alag color ka ho
colors = ['red', 'blue', 'green', 'orange']
plt.bar(friends, pocket_money, color=colors)

# Graph ko Title aur Labels dena
plt.title("Monthly Pocket Money Comparison")
plt.xlabel("Friends")
plt.ylabel("Pocket Money (in Rupees)")

# Graph ko screen par dikhana
plt.show()

print("Graph is displayed on your screen! You can easily see that Sneha has the highest pocket money.")
