import random

NFL_TEAMS = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']
NFL_TEAMS_SHORT = [(team.split()[-1]) for team in NFL_TEAMS]

while True:
    userready = input("~~~Are you ready to start the draft? (y/n)~~~")
    if userready.lower() == 'n':
        raise ValueError("Come back when you're ready!")
    elif userready.lower() == 'y':
        break
    else:
        print("Please enter a valid answer!")

PLAYERS = []
PLAYERS_COUNT = 0
while True:
    newplayer = input("Enter Player's Name (or 'ready'?): ")
    if newplayer.lower() == 'ready' # also make sure at least two players??:
        break
    if newplayer.lower() in [x.lower() for x in PLAYERS]:
        print("Name already exists!")
    else:
        PLAYERS.append(newplayer)
PLAYERS_COUNT = len(PLAYERS)

random.shuffle(PLAYERS)

# HOW DO I MAKE DRAFT LOOP CHECK FOR VALID ENTRY
while NFL_TEAMS_SHORT != 0:
    for players in PLAYERS:
        teaminput = True
        try:
            teaminput = input(f"{player}, choose your team:")
            assert teaminput in NFL_TEAMS_SHORT
        except:
            print("Please enter a valid team name!")
            continue

while NFL_TEAMS_SHORT != 0:
    for player in PLAYERS:
        inputted = True
        while inputted not in NFL_TEAMS_SHORT:
            inputted = input(f"{player}, choose your team:")
            try:
               inputted in NFL_TEAMS_SHORT 
            except:
                print("Please enter a valid team name!")
                continue
        NFL_TEAMS_SHORT.remove(inputted)



# FUNCTION Declare number of players, with names
## OR just use same names
# Determine random order

# FUNCTION draft
# Insert into spreadsheet

# FUNCTION metrics/stats call
# Web scrape
# Lena lecture beautiful soup 11/12
