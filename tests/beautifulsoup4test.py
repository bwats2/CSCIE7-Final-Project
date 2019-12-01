import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
# https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486
NFL_TEAMS = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']
website_url  = requests.get("https://en.wikipedia.org/wiki/2019_NFL_season").text
soup = BeautifulSoup(website_url,"html.parser")
my_table = soup.find('table',{'class':'multicol'})
links = my_table.find_all('td')
teamscores = [link.text.strip() for link in links] # Take text between tags, and strip special characters
print(teamscores)
teamscoredict = defaultdict(int) # Dict to hold teams and scraped score values
for team in NFL_TEAMS:
    # Wikipedia sometimes adds characters to start or end of team name in table
    # https://stackoverflow.com/questions/4146009/python-get-list-indexes-using-regular-expression
    teamindex = [i for i, word in enumerate(teamscores) if word.endswith(team) or word.startswith(team)]
    wins = int(teamscores[teamindex[0]+1])
    ties = int(teamscores[teamindex[0]+3])
    score = wins+ties/2 # Full point for win, half point for tie
    teamscoredict[team] = score
print(teamscoredict)