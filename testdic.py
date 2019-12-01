import csv 
dic = {'Jeremy Simon': ['New England Patriots', 'Pittsburgh Steelers', 'Seattle Seahawks', 'Minnesota Vikings', 'New Orleans Saints', 'Indianapolis Colts', 'Miami Dolphins', 'Denver Broncos'], 'Koo': ['Tennessee Titans', 'Philadelphia Eagles', 'San Francisco 49ers', 'Kansas City Chiefs', 'Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Houston Texans'], 'Brian': ['Tampa Bay Buccaneers', 'Oakland Raiders', 'New York Giants', 'Los Angeles Rams', 'Cleveland Browns', 'Green Bay Packers', 'Buffalo Bills', 'Cincinnati Bengals'], 'Butes': ['Washington Redskins', 'New York Jets', 'Jacksonville Jaguars', 'Los Angeles Chargers', 'Dallas Cowboys', 'Detroit Lions', 'Carolina Panthers', 'Chicago Bears']}
for key, value in dic.items():
    print(key, value)

# https://realpython.com/iterate-through-dictionary-python/#iterating-through-values

# with open('teamschosendict.csv', mode='w') as f:
#             fwriter = csv.writer(f)
#             for key, value in dic:
#                     fwriter.writerow(key)
#                     fwriter.writerow(value)

#https://stackoverflow.com/questions/10373247/how-do-i-write-a-python-dictionary-to-a-csv-file
with open('teamschosendict.csv','w', newline='') as f:
    w = csv.writer(f)
    w.writerow(dic.keys())
    w.writerow(dic.values())
