import csv 

lst = []
with open('teamschosendict.csv','r') as f: 
    r = csv.reader(f)
    for row in r:
        lst.append(row)
return lst
