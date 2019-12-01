from collections import defaultdict
import csv

dic = defaultdict(list)
def checkKeyAndAdd(dic, key, team):  
    dic[key].append(team)
        
checkKeyAndAdd(dic, "Brian", "Panthers")
checkKeyAndAdd(dic, "Brian", "Pats")
checkKeyAndAdd(dic, "Brian", "Eagles")
checkKeyAndAdd(dic, "Nat", "chiefs")
checkKeyAndAdd(dic, "Brian", "Redkins")
checkKeyAndAdd(dic, "Nat", "Titans")
checkKeyAndAdd(dic, "Nat", "rams")



print(dic)
with open('teamschosendict.csv','w', newline='') as f:
    w = csv.writer(f)
    w.writerow(dic.keys())
    w.writerow(dic.values())

# player = 'Brian'
# print(f"Brian's teams are: {dic[player]}")
