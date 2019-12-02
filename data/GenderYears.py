import matplotlib.pyplot as plt

Years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1968, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

MenMedals = [9, 12, 14, 13, 17, 16, 17, 17, 18, 23, 23, 0, 23, 0, 23, 25]

WomenMedals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20, 19, 21, 21]

plt.plot(Years, MenMedals, color=('#b9dafe'), linewidth=3.0)
plt.plot(Years, WomenMedals, color=('#fbc8cf'), linewidth=3.0)


plt.ylabel("Evolution of Medal Counts")
plt.xlabel("Evolution of Medal Counts by Years")
plt.title("Evolution of Medal Counts by Gender 1924-2015", pad=20)

# show the chart
plt.show()