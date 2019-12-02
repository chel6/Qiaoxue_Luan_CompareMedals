import matplotlib.pyplot as plt

Years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1968, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

GoldMedals = [9, 12, 14, 0, 17, 16, 0, 0, 0, 0, 0, 0, 43, 19, 44, 46]

SilverMedals = [0, 0, 0, 13, 0, 0, 0, 17, 0, 23, 23, 20, 0, 0, 0, 0]

BronzeMedals = [0, 0, 0, 0, 0, 0, 17, 0, 18, 0, 0, 0, 0, 0, 0, 0]

plt.plot(Years, GoldMedals, color=('gold'), linewidth=3.0)
plt.plot(Years, SilverMedals, color=('silver'), linewidth=3.0)
plt.plot(Years, BronzeMedals, color=('darkgoldenrod'), linewidth=3.0)


plt.ylabel("Evolution of Medal Counts")
plt.xlabel("Evolution of Different Medal Counts by Years")
plt.title("Evolution of Different Medal Counts 1924-2015", pad=20)


# show the chart
plt.show()