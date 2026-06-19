# ==========================================
# Codeaura Python Course: 04_seaborn_advanced_styling.py
# ==========================================
# Concept: Seaborn Library (Data Visualization on Steroids)
# Seaborn library Matplotlib ke upar bani hai, lekin iske graphs automatically bahut professional aur sundar hote hain.
# Real Life Example: Ek restaurant me aane wale customers ka Data (Total bill vs Tip).

import seaborn as sns
import matplotlib.pyplot as plt

print("Loading Restaurant Dataset and Creating Advanced Graph...")

# Seaborn ke andar pehle se hi kuch sample datasets hote hain practice ke liye.
# Hum 'tips' naam ka ek restaurant dataset load kar rahe hain.
tips_data = sns.load_dataset("tips")

# Ab hum ek 'Scatter Plot' (Bindiyo wala graph) banayenge.
# Ye dekhega ki kya zyada khana khane wale (Total Bill) zyada Tip bhi dete hain?
# sns.scatterplot() is used to create this.
# 'hue="time"' ka matlab hai Lunch aur Dinner ki bindiyo ka color alag hoga!

sns.set_theme(style="darkgrid") # Isse piche ka background professional dark grid ban jayega
sns.scatterplot(data=tips_data, x="total_bill", y="tip", hue="time", size="size", sizes=(20, 200))

plt.title("Restaurant Data: Total Bill vs Tip")
plt.xlabel("Total Bill (in Dollars)")
plt.ylabel("Tip (in Dollars)")

# Graph ko screen par dikhana
plt.show()

print("Graph is displayed! Notice how beautiful and professional this Seaborn graph looks compared to basic Matplotlib.")
