def checkKeyAndAdd(dic, key, team):  
    if key in dic: 
        dic[key].append(team)
    else: 
        dic[key]=[]
        dic[key].append(team)
        
dict = {}
checkKeyAndAdd(dict, "Brian", "Panthers")
checkKeyAndAdd(dict, "Brian", "Pats")
checkKeyAndAdd(dict, "Brian", "Eagles")
checkKeyAndAdd(dict, "Nat", "chiefs")
checkKeyAndAdd(dict, "Brian", "Redkins")
checkKeyAndAdd(dict, "Nat", "Titans")
checkKeyAndAdd(dict, "Nat", "rams")



print(dict)
player = 'Brian'
print(f"Brian's teams are: {dict[player]}")
