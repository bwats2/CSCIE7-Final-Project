import random  # Random used to shuffle draft order
import csv  # CSV used to store data
from typing import List, Dict  # Allow type hint for lists, dict
from collections import defaultdict  # Allows us to use defaultdict instead of lbyl, per class
import requests  # Needed for webscraping
from bs4 import BeautifulSoup  # Needed for webscraping


# Declare global list variables containing teams and teams short names
NFL_TEAMS_MAIN = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']
NFL_TEAMS_SHORT_MAIN = [(team.split()[-1]) for team in NFL_TEAMS_MAIN]


def load_menu():
    "Prints the starting/default menu for the draft process, and directs user to function based on input"
    while True:
        print("\n~~WELCOME TO THE SNEK DRAFT!~~") # My friends have always called it 'Snek' instead of 'Snake' as a joke
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
        elif inputtedz == "webscrape": # 'Hidden' developer option to see all webscraped data
            print(webscrape())
        elif inputtedz=="readplayers": # 'Hidden' developer option to see all players
            print(read_players())
        elif inputtedz=="readdraft": # 'Hidden' developer option to see players with teams drafted
            readplayers = read_draft()
            for i in range(len(readplayers[0])):
                print(readplayers[0][i])
                print(readplayers[1][i])
        elif inputtedz=="sms":
            smstest()
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
            if (len(PLAYERS) >= 2) and (len(NFL_TEAMS_MAIN)%len(PLAYERS))==0: # Checks if appropriate number of players entered
                print("\tSaving players and shuffling draft order!")
                random.shuffle(PLAYERS) # Shuffle player order
                with open('players.csv',mode='w', newline='') as f: # https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
                    fwriter = csv.writer(f)
                    for player in PLAYERS:
                        fwriter.writerow([player])
                break
            print('\tYou need at least 2 players, AND a factor of 32!')
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
    i = 0 # Counter to store draft selection number
    for player in PLAYERSTOTAL:
        while True and i != 32:
            inputted = input(f"\n{player}, choose a team: ")
            if inputted in ('exit', 'Exit'):
                raise Exception("EXITING") # Allow exit of draft
            try: # Try-Except block to ensure valid team name entered
                inputted_team = NFL_TEAMS[NFL_TEAMS_SHORT.index(inputted)]
                del NFL_TEAMS[NFL_TEAMS_SHORT.index(inputted)] # Deleting chosen teams from list
                del NFL_TEAMS_SHORT[NFL_TEAMS_SHORT.index(inputted)]
                print(f"\tThese are the {len(NFL_TEAMS)} teams left: {NFL_TEAMS}")
                checkKeyAndAdd(dic, player, inputted_team)
                i+=1
                break
            except:
                print("\tERROR. Enter a valid team name OR team already taken. Ex/Enter 'Patriots' for the 'New England Patriots'.")
    with open('teamschosendict.csv','w', newline='') as f: # https://stackoverflow.com/questions/10373247/how-do-i-write-a-python-dictionary-to-a-csv-file
        w = csv.writer(f)
        w.writerow(dic.keys()) # Storing players as row 1
        w.writerow(dic.values()) # Storing teams chosen by players as row 2
    print("The DRAFT is done!")


def webscrape() -> Dict:
    "Scrapes web data into dictionary that gets returned"
    # https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
    # https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486
    NFL_TEAMS = NFL_TEAMS_MAIN[:]
    website_url  = requests.get("https://en.wikipedia.org/wiki/2019_NFL_season").text
    soup = BeautifulSoup(website_url,"html.parser")
    my_table = soup.find('table',{'class':'multicol'}) # Based on inspecting source code
    links = my_table.find_all('td')
    teamscores = [link.text.strip() for link in links] # Take text between tags, and strip special characters
    teamscoredict = defaultdict(int) # Dict to hold teams and scraped score values
    for team in NFL_TEAMS:
        # Wikipedia sometimes adds characters to start or end of team name in table
        # https://stackoverflow.com/questions/4146009/python-get-list-indexes-using-regular-expression
        teamindex = [i for i, word in enumerate(teamscores) if word.endswith(team) or word.startswith(team)]
        wins = int(teamscores[teamindex[0]+1])
        ties = int(teamscores[teamindex[0]+3])
        score = wins+ties/2 # Full point for win, half point for tie
        teamscoredict[team] = score
    return teamscoredict # Return dict


def read_draft() -> List:
    "Reads draft results from csv into a list"
    lst = []
    with open('teamschosendict.csv','r') as f: 
        r = csv.reader(f)
        for row in r:
            lst.append(row)
    return lst # lst[0] contains players, lst[1] contains teams


def player_metrics():
    "Returns in descending order list of players based on current scores"
    scrapedict = webscrape() # Runs the webscrape
    draftresults = read_draft() # Reads from csv
    if len(draftresults)==0: # Checks if draft happened
        print("You haven't drafted teams - do the draft and try again!\n")
        load_menu()
    playertotals = defaultdict(int)
    i = 0
    for i in range(len(draftresults[0])): # Iterate over number of players
        sumz = 0 # Set counter for sum
        for team in eval(draftresults[1][i]):
            sumz += scrapedict.get(team)
        playertotals[draftresults[0][i]] = sumz      
    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    # https://thispointer.com/python-how-to-sort-a-dictionary-by-key-or-value/
    print("\nCurrent order of players from first to last: ")
    print("----------------------")
    smslist = [(f"{key}-{value}") for (key, value) in sorted(playertotals.items() , reverse=True, key=lambda x: x[1])] # Sorts and prints dictionary from high to low based on values
    return smslist

from twilio.rest import Client
def smstest():
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("AC45ba5f20797586501e0121bc5614e71e", "401c57f94e2f0fa07ff291b40b6793d6")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    smss=player_metrics()
    client.messages.create(to="+15084981772",
                           from_="+12512449701",
                           body=f"Current SNEK results: {smss}")


if __name__ == '__main__':
    load_menu() # Loads menu when called
    