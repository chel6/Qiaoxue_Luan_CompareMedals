import numpy as np
import matplotlib.pyplot as plt
 
# Make a fake dataset:
height = [3, 22, 50, 351, 159,40]
bars = ('Biathlon', 'Bobsleigh', 'Curling', 'Ice_Hockey', 'Skating','Skiing')
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height, color=['#a6c9c9', '#ebe38a', '#debfca', '#c76082', '#5d818b', '#fabc5a'])
plt.xticks(y_pos, bars)

 
# Create names on the x-axis
plt.ylabel("How Many Medals")
plt.xlabel("Which Sport")
plt.title("Which Sport does Canada Won the Most Medals.", pad=20)
# Show graphic
plt.show()

