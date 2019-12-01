# import matplotlib.pyplot as plt

# years = [1920, 1950, 1970, 1980,1985, 1990, 1995, 2000, 2005, 2010, 2015]

# pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9]

# plt.plot(years, pops, color=(255/255, 100/255, 100/255), linewidth=6.0)

# plt.ylabel("World Population by Billions")
# plt.xlabel("Population Growth by Year")
# plt.title("Global Population Growth 1900-2015", pad=20)

# # show the chart
# plt.show()
import csv
import matplotlib.pyplot as plt

years = [1920, 1950, 1970, 1980,1985, 1990, 1995, 2000, 2005, 2010, 2015]

men.number =[]
women.number = []
men = []
women = []

categories=[] #first row->not data
with open('data/canada_icehockey.csv') as csvfile:
	reader=csv.reader(csvfile)
	line_count=0
	
	for row in reader:
		if line_count is 0:
			print("this is the first row in the spreadsheet")
			categories.append(row)
			line_count+=1

		else:
			if row[5]== "Men":
				print("Men won a medal")
				men.append(row[5])
				men.number = number +1

			else:
				print("Women won a metal")
				women.append(row[5])
				women.number = number +1

		print(line_count)
		line_count+=1

#now we can see our medal counts
print(len(women),"Women won a medal")
print(len(men),"Men won a medal")

plt.plot(years, pops, color=('#fbc8cf','#b9dafe'), linewidth=6.0)
plt.ylabel("How Many Medals")
plt.xlabel("Year")
plt.title("Medals Growth 1920-2015", pad=20)

explode=(0.1,0.1)