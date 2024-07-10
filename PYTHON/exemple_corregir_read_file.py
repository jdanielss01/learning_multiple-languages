import csv

with open('experiment.csv') as file:
    reader = csv.reader(file, delimiter=',')
for row in reader:
	print (row)
  
