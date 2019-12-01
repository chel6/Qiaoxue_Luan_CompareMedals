import csv
import matplotlib.pyplot as plt

men=[]
women=[]

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

			 else:
				 print("Women won a metal")
				 women.append(row[5])

		 print(line_count)
		 line_count+=1

#now we can see our medal counts
print(len(women),"Women won a medal")
print(len(men),"Men won a medal")

labels=["Women","Men","Bronze"]
sizes=[len(women),len(men)]
colors=['#fbc8cf','#b9dafe']
explode=(0.1,0.1)

plt.pie(sizes,explode=explode,colors=colors,autopct='%1.f%%',shadow=True,startangle=140)

plt.axis("equal")

plt.legend(labels,loc=1)
plt.title("Who Won More Medals?")
plt.xlabel("Metal Counts Since 1924")
plt.show()