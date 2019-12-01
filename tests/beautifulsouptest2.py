import requests
from bs4 import BeautifulSoup
import re
# https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
# https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486

NFL_TEAMS = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']

website_url  = requests.get("https://en.wikipedia.org/wiki/2019_NFL_season").text

soup = BeautifulSoup(website_url,"html.parser")
print(soup.prettify())
# my_table = soup.find('table',{'class':'wikitable'}) # Changed to wikitable
# print(my_table)
# links = my_table.find_all('td')
# print(links)
# teamscores = []
# for link in links:
#     # teamscores.append(link.text.strip())
# print(teamscores)
# index = teamscores.index("New Orlean Saints")
# print(teamscores[index])
# print(teamscores[index+1])
# print(teamscores[index+2])
# Issue is that team names have added characters such as "y – New Orleans Saints"