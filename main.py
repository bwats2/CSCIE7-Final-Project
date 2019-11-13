import random

NFL_TEAMS = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']
NFL_TEAMS_SHORT = [(team.split()[-1]) for team in NFL_TEAMS]

PLAYERS = []
PLAYERS_COUNT = 0
while True:
    inputted = input("Enter Player's Name (or 'exit'?): ")
    if inputted.lower() == 'exit':
        break
    PLAYERS.append(inputted)
PLAYERS_COUNT = len(PLAYERS)

random.shuffle(PLAYERS)

while NFL_TEAMS_SHORT != 0:
    for players in PLAYERS:
        inputted = True
        try:
            inputted = input(f"{player}, choose your team:")
            assert inputted in NFL_TEAMS_SHORT
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
