# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.2
 
# set height of bar

GoldMedals = [81, 139]
SilverMedals = [20, 76]
BronzeMedals = [0, 35]
 
# Set position of bar on X axis

r1 = np.arange(len(GoldMedals))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot

plt.bar(r1, GoldMedals, color='gold', width=barWidth, edgecolor='white', label='Gold Medals')
plt.bar(r2, SilverMedals, color='silver', width=barWidth, edgecolor='white', label='Silver Medals')
plt.bar(r3, BronzeMedals, color='darkgoldenrod', width=barWidth, edgecolor='white', label='Bronze Medals')
 
# Add xticks on the middle of the group bars
# plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(GoldMedals))], ['Women', 'Men'])

plt.ylabel("Medal Counts")
plt.xlabel("Medal Counts by Gender")
plt.title("Gender Comparison of Gold, Silver and Bronze Medals 1924-2015", pad=20)
 
# Create legend & Show graphic
plt.legend()
plt.show()