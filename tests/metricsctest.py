# This function will scrape wikipedia data into dictionary
# Then team names per player will be run over dictionary with scores added into dict of player: score
# Then dict will be sorted
# Then will print out for item in dict, first player, "Followed by __ with xx points"
import random # Random used to shuffle draft order
import csv # CSV used to store data
from typing import List, Dict # Allow type hint for lists
from collections import defaultdict # Allows us to use defaultdict instead of lbyl, per class
import requests # Needed for webscraping
from bs4 import BeautifulSoup # Needed for webscraping

# Declare global list variables containing teams and teams short names
NFL_TEAMS_MAIN = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']
NFL_TEAMS_SHORT_MAIN = [(team.split()[-1]) for team in NFL_TEAMS_MAIN]

def webscrape() -> Dict:
    "Scrapes web data into dictionary that gets returned"
    # https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
    # https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486
    NFL_TEAMS = NFL_TEAMS_MAIN[:]
    website_url  = requests.get("https://en.wikipedia.org/wiki/2019_NFL_season").text
    soup = BeautifulSoup(website_url,"html.parser")
    my_table = soup.find('table',{'class':'multicol'})
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

import operator
def read_draft() -> List:
    lst = []
    with open('teamschosendict.csv','r') as f: 
        r = csv.reader(f)
        for row in r:
            lst.append(row)
    return lst


"Scrapes web data to provide total sum score of players' teams, and who is winning."
scrapedict = webscrape()
draftresults = read_draft()
if len(draftresults)==0: # Checks if draft happened
    print("You haven't drafted teams - do the draft and try again!\n")
    load_menu()
playertotals = defaultdict(int)
i = 0
for i in range(len(draftresults[0])): # Iterate over number of players
    sum = 0
    for team in eval(draftresults[1][i]):
        sum += scrapedict.get(team)
    playertotals[draftresults[0][i]] = sum       
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# sorted_x = sorted(playertotals.items(), key=operator.itemgetter(1))
# sorted_x.reverse()
# print(sorted_x)
	
# Use List comprehension to print the contents of dictionary , sorted by value
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# https://thispointer.com/python-how-to-sort-a-dictionary-by-key-or-value/
print("Current order of players from first to last: ")
print("-----")
[print(key, "-", value) for (key, value) in sorted(playertotals.items() , reverse=True, key=lambda x: x[1])]