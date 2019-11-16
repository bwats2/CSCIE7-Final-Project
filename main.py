import sys
import random
import csv

NFL_TEAMS = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']
NFL_TEAMS_SHORT = [(team.split()[-1]) for team in NFL_TEAMS]

#Seperate functions for seperate stages?
#Store data in csv or database?


def register_players():
    PLAYERS = []
    # PLAYERS_COUNT = 0
    # global PLAYERS
    # global PLAYERS_COUNT 
    while True:
        if len(PLAYERS) > 0:
            print(f"\nCurrent Players: ({len(PLAYERS)}) {PLAYERS}")
        newplayer = input("  Enter Player's Name (or 'ready'?): ")
        if newplayer.lower() == 'delete':
            if len(PLAYERS) < 1:
                print("\tNothing to delete!")
            else:
                print(f"\tDeleting {PLAYERS[-1]}")
                PLAYERS.pop(-1)
        elif newplayer.lower() == 'ready':
            if len(PLAYERS) >= 2:
                print("\tSaving players and shuffling draft order!")
                return
            print('\tYou need at least 2 players!')
        elif newplayer.lower() == 'exit':
                print("\tEXITING...")
                del PLAYERS[:]
                print("\t...All players deleted!")
                return
        elif newplayer.lower() in [x.lower() for x in PLAYERS]:
            print("\tName already exists!")
        elif newplayer in (""," ","   "):
            print("\tEnter a valid name!")
        else:
            PLAYERS.append(newplayer)
    # PLAYERS_COUNT = len(PLAYERS)
    random.shuffle(PLAYERS)

    with open('players.csv',mode='w') as f:
        fwriter = csv.writer(f, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for player in PLAYERS:
            fwriter.writerow([player])


def read_players(): # Type Hint?
    PLAYERSREAD = []
    # PLAYERSCOUNT = 0
    with open('players.csv',mode='r') as f:
        freader = csv.reader(f, delimiter=',')
        for row in freader:
            # print(row)
            if row != []: # Bug where csv writer adds extra lines here, but not appearing in ED environment
                for item in row:
                    PLAYERSREAD.append(item)
                # PLAYERSCOUNT += 1
    return(PLAYERSREAD)


def the_draft():
    global NFL_TEAMS
    global NFL_TEAMS_SHORT
    
    PLAYERS = read_players()
    PLAYERSTOTAL = ((PLAYERS+PLAYERS[::-1])*int(len(NFL_TEAMS)/len(PLAYERS)))
    
    i = 0
    while len(NFL_TEAMS) > 0:
        for player in PLAYERSTOTAL:
            inputted = input(f"\n{player}, choose a team: ")
            print(inputted)
            inputted_team = NFL_TEAMS[NFL_TEAMS_SHORT.index(inputted)]
            del NFL_TEAMS[NFL_TEAMS_SHORT.index(inputted)]
            del NFL_TEAMS_SHORT[NFL_TEAMS_SHORT.index(inputted)]
            print(f"\tThese are the teams left: {NFL_TEAMS}") # Can I print items in list comma sep?
            i += 1
            with open('teamschosen.csv',mode='a') as f: # a means append
                fwriter = csv.writer(f, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
                fwriter.writerow([i, player, inputted_team])
    print("The DRAFT is done!")
    return

def player_metrics():
    pass


# def print_players():
#     print(PLAYERS)

# def the_draft():
#     while True:
#         userready = input("~~~ Are you ready to start the draft? (y/n) ~~~")
#         if userready.lower() == 'n':
#             raise ValueError("Come back when you're ready!")
#         elif userready.lower() == 'y':
#             break
#         else:
#             print("Please enter a valid answer!")




#     # HOW DO I MAKE DRAFT LOOP CHECK FOR VALID ENTRY
#     while NFL_TEAMS_SHORT != 0:
#         for players in PLAYERS:
#             teaminput = True
#             try:
#                 teaminput = input(f"{player}, choose your team:")
#                 assert teaminput in NFL_TEAMS_SHORT
#             except:
#                 print("Please enter a valid team name!")
#                 continue

#     while NFL_TEAMS_SHORT != 0:
#         for player in PLAYERS:
#             inputted = True
#             while inputted not in NFL_TEAMS_SHORT:
#                 inputted = input(f"{player}, choose your team:")
#                 try:
#                 inputted in NFL_TEAMS_SHORT 
#                 except:
#                     print("Please enter a valid team name!")
#                     continue
#             NFL_TEAMS_SHORT.remove(inputted)



# FUNCTION Declare number of players, with names
## OR just use same names
# Determine random order

# FUNCTION draft
# Insert into spreadsheet

# FUNCTION metrics/stats call
# Web scrape
# Lena lecture beautiful soup 11/12




if __name__ == '__main__':
    globals()[sys.argv[1]]()
