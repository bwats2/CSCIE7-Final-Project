import csv

team_list = []    # Store NFL Team Names
names = set()    # Store player names
with open('data 2019 CSV.csv') as csvfile:
    csvfile.readline()
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        x = row[1]    # Second Column, contains Team Names
        team_list.append(x)
        y = row[2]    # Third Column, contains People Names
        names.add(y)

for item in team_list:
    print(item, len(item.split()))

names.remove('Alex il Butte')
names.add('Alex Butensky')
print(names)
