import random
import csv
PLAYERS = []
PLAYERS_COUNT = 0

while True:
    newplayer = input("Enter Player's Name (or 'ready'?): ")
    if newplayer.lower() == 'ready':
        if len(PLAYERS) > 2:
            break
        print('You need more than just 1 player!')
    if newplayer.lower() == 'exit':
            print("EXITING")
            del PLAYERS[:]
            break
    if newplayer.lower() in [x.lower() for x in PLAYERS]:
        print("Name already exists!")
    else:
        PLAYERS.append(newplayer)
# PLAYERS_COUNT = len(PLAYERS)
random.shuffle(PLAYERS)

with open('players.csv',mode='w') as f:
    fwriter = csv.writer(f, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for player in PLAYERS:
        fwriter.writerow([player])