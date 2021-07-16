import matplotlib.pyplot as plt
import csv

from numpy.core.defchararray import index
from numpy.lib.function_base import median


''''
Go through years.

create list of new indexs.

split array into more arrays

perform median operation of splitted arrays

records results and years
'''

x = []
y =[]

with open('GCF.csv', 'r') as csvFile:
    plots = csv.reader(csvFile, delimiter = ',')
    firstRow = True
    for row in plots:
        if firstRow == True:
            firstRow = False
        else:
           # x.append(int(row[0]))
            date = row[0]
            date = date[0:4]
            x.append(date)
            y.append(row[1])
            print('workin')



indexList = []

year = []
median_points = []

for i in range(0, len(x) - 1):
    if x[i + 1] > x[i]:
        indexList.append(i+ 1)

firstPass = True

for q in range (0, len(indexList) - 2):
    count = q
    new_array = []

    if firstPass == True:

        for l in range(0, indexList[count]):
            if y[l] != 'null':
                new_array.append(float(y[l]))
        
        year.append(x[l])
        val = median(new_array)
        median_points.append(val)
        firstPass = False
    
    if firstPass == False:
        for b in range(indexList[count], indexList[count + 1]):
            if y[b] != 'null':
                new_array.append(float(y[b]))

        year.append(x[b])
        val = median(new_array)
        median_points.append(val)


plt.plot(year, median_points)

plt.show()