# TODO: Type Hints?
import random # Random used to shuffle draft order
import csv # CSV used to store data
from typing import List # Allow type hint for lists
from collections import defaultdict # Allows us to use defaultdict instead of lbyl, per class


# Declare global list variables containing teams and teams short names
NFL_TEAMS_MAIN = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']
NFL_TEAMS_SHORT_MAIN = [(team.split()[-1]) for team in NFL_TEAMS]


def load_menu():
    "Prints the starting/default menu for the draft process, and directs user to function based on input"
    while True:
        print("\n~~WELCOME TO THE SNEK DRAFT!~~")
        print("1 - Register Players!")
        print("2 - Start the Draft!")
        print("3 - Get the Stats!")
        print("4 - EXIT")
        print("====================")
        inputtedz = input("Select an option: ")
        if inputtedz == "1":
            register_players()
        elif inputtedz == "2":
            the_draft()
        elif inputtedz == "3":
            player_metrics()
        elif inputtedz == "4":
            break
        else:
            print("\t~~ERROR: Please enter a valid choice!~~")
        

def register_players():
    "Takes user through the player registration process"
    PLAYERS = [] # Init list to hold players
    while True:
        # Erases any existing data by wiping file clean
        with open('players.csv', 'r+') as f:# https://stackoverflow.com/questions/29579448/how-to-delete-a-csv-file-in-python
            f.truncate(0) # "Need '0' when using r+"", per source above
        if len(PLAYERS) > 0: # Prints list of current players if a player has been entered
            print(f"\nCurrent Players: ({len(PLAYERS)}) {PLAYERS}")
        newplayer = input("  Enter Player's Name (or 'ready'?): ")
        if newplayer.lower() == 'delete': # Allows player to delete last entered
            if len(PLAYERS) < 1: # Checks if there is something to delete
                print("\tNothing to delete!")
            else:
                print(f"\tDeleting {PLAYERS[-1]}") # Deletes last player entered
                PLAYERS.pop(-1)
        elif newplayer.lower() == 'ready':
            if len(PLAYERS) >= 2: # Checks if appropriate number of players entered
                print("\tSaving players and shuffling draft order!")
                random.shuffle(PLAYERS) # Shuffle player order
                with open('players.csv',mode='w', newline='') as f: # https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
                    fwriter = csv.writer(f)
                    for player in PLAYERS:
                        fwriter.writerow([player])
                break
            print('\tYou need at least 2 players!')
        elif newplayer.lower() == 'exit': # Allows user to exit stage
                print("\tEXITING...")
                del PLAYERS[:]
                print("\t...All players deleted!")
                break
        elif newplayer.lower() in [x.lower() for x in PLAYERS]: # Checks if name already entered
            print("\tName already exists!")
        elif newplayer.strip() == "": # Prevents blank/empty names
            print("\tEnter a valid name!")
        else:
            PLAYERS.append(newplayer) # Adds player to the list


def read_players() -> List:
    "Reads players from csv file, and returns list of players"
    PLAYERSREAD = [] # Init list to store players read from csv
    with open('players.csv',mode='r') as f:
        freader = csv.reader(f, delimiter=',')
        for row in freader:
            for item in row:
                PLAYERSREAD.append(item)
    return(PLAYERSREAD) # Return list of players read


def checkKeyAndAdd(dic, key, team):  
    "Checks if player and team in dict, and adds to list in value"
    dic[key].append(team) # Defaultdict(list) means it will init list for keys, and we don't have to lbyl


def the_draft():
    "Takes user through the draft process"
    with open('teamschosendict.csv', 'r+') as f: #erase existing data
        f.truncate(0)
    NFL_TEAMS = NFL_TEAMS_MAIN[:]
    NFL_TEAMS_SHORT = NFL_TEAMS_SHORT_MAIN[:]
    PLAYERS = read_players()
    if len(PLAYERS)==0: # Checks if there are players registered
        print("You haven't registered any players - register some players and try again!\n")
        load_menu()
    else:
        PLAYERSTOTAL = ((PLAYERS+PLAYERS[::-1])*int(len(NFL_TEAMS)/len(PLAYERS))+PLAYERS[:(len(NFL_TEAMS)%len(PLAYERS))]) # Creates full list of players order in snake chain
    dic = defaultdict(list)
    i = 0
    for player in PLAYERSTOTAL:
        while True and i != 32:
            inputted = input(f"\n{player}, choose a team: ")
            try: # Try-Except block to ensure valid team name entered
                inputted_team = NFL_TEAMS[NFL_TEAMS_SHORT.index(inputted)]
                del NFL_TEAMS[NFL_TEAMS_SHORT.index(inputted)]
                del NFL_TEAMS_SHORT[NFL_TEAMS_SHORT.index(inputted)]
                print(f"\tThese are the {len(NFL_TEAMS)} teams left: {NFL_TEAMS}")
                checkKeyAndAdd(dic, player, inputted_team)
                i+=1
                break
            except:
                print("\tERROR. Enter a valid team name OR team already taken. Ex/Enter 'Patriots' for the 'New England Patriots'.")
    with open('teamschosendict.csv','w', newline='') as f: # https://stackoverflow.com/questions/10373247/how-do-i-write-a-python-dictionary-to-a-csv-file
        w = csv.writer(f)
        w.writerow(dic.keys())
        w.writerow(dic.values())
    print("The DRAFT is done!")
    load_menu()


def player_metrics():
    "Scrapes web date to provide total sum score of players' teams, and who is winning."
    pass


if __name__ == '__main__':
    # globals()[sys.argv[1]]() # Runs function directly that is called as argv[1]
    load_menu()
