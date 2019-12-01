import requests
from bs4 import BeautifulSoup
# https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
# https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486

NFL_TEAMS = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']

website_url  = requests.get("https://en.wikipedia.org/wiki/2019_NFL_season").text

soup = BeautifulSoup(website_url,"html.parser")
# print(soup.prettify())
my_table = soup.find('table',{'class':'multicol'})
# print(my_table)
links = my_table.find_all('td')
# print(links)
teamscores = [link.text.strip() for link in links]
# for link in links:
#     teamscores.append(link.text.strip())
print(teamscores)
# index = teamscores.index("New Orlean Saints")
# print(teamscores[index])
# print(teamscores[index+1])
# print(teamscores[index+2])

# Issue is that team names have added characters such as "y – New Orleans Saints"
# Maybe I can use REGEX???


# import re
# # berry_idx = [i for i, item in enumerate(NFL_TEAMS) if re.search('??????New Orlean Saints?????')]
# teamindex = [i for i, word in enumerate(teamscores) if word.endswith('New England Patriots') or word.startswith('New England Patriots')]
# print(teamindex[0])

# https://stackoverflow.com/questions/4146009/python-get-list-indexes-using-regular-expression
from collections import defaultdict

teamscoredict = defaultdict(int) # Dict to hold team and score value
for team in NFL_TEAMS:
    print(team)
    # Wikipedia sometimes adds characters to start or end of team name in table
    teamindex = [i for i, word in enumerate(teamscores) if word.endswith(team) or word.startswith(team)]
    print(teamscores[teamindex[0]])
    wins = int(teamscores[teamindex[0]+1])
    ties = int(teamscores[teamindex[0]+3])
    score = wins+ties/2
    print(f"wins: {wins}")
    print("losses: ",teamscores[teamindex[0]+2])
    print(f"ties: {ties}")
    print(score)
    teamscoredict[team] = score
print(teamscoredict)