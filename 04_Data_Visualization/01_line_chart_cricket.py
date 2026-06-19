# ==========================================
# Codeaura Python Course: 01_line_chart_cricket.py
# ==========================================
# Concept: Line Chart (Samay ke sath koi cheez kaise badhti/ghatti hai)
# Real Life Example: Virat Kohli ke pehle 5 matches ke runs.

import matplotlib.pyplot as plt

# X-axis (Neeche wali line): Matches
matches = ["Match 1", "Match 2", "Match 3", "Match 4", "Match 5"]

# Y-axis (Khadi line): Runs scored
runs = [12, 45, 82, 104, 56]

print("Creating Cricket Line Chart...")

# Plotting the line
# marker='o' means har point par ek gol dot (dot) aayega
# color='b' means Blue line, linestyle='--' means dashed line
plt.plot(matches, runs, marker='o', color='b', linestyle='--', linewidth=2)

# Graph ko Title aur Labels dena (Bahut zaroori hai taki samajh aaye ki graph kis baare me hai)
plt.title("Virat Kohli - Runs in First 5 Matches")
plt.xlabel("Matches Played")
plt.ylabel("Runs Scored")

# Graph me piche ek grid (jaal) banana taki read karna aasan ho
plt.grid(True)

# Graph ko screen par dikhana
plt.show()

print("Graph is displayed on your screen! Close the graph window to continue.")
