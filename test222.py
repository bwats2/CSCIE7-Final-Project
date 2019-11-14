import csv
PLAYERSREAD = []
with open('players.csv',mode='r') as f:
    freader = csv.reader(f, delimiter=',')
    for row in freader:
        PLAYERSREAD.append(row)
print(PLAYERSREAD)