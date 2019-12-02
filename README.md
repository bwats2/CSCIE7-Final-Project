# CSCIE7 Final Project: Snek Draft (README.md)

## Describe the Problem:
**Snek Draft** was built to automate what is currently a manual process amongst my friends. For the past 4 years we have been participating in an informal snake-chain fantasy football draft (the ‘snake’ describes the way teams are drafted; ['snek'](https://knowyourmeme.com/memes/snek) is due to internet memes and millenial humor). We randomly choose an order, and then take turns drafting. We record who chose what team-by-team by searching through a spreadsheet and writing their name next to the team name. Only recently did we start using IMPORTRANGE to pull data into the spreadsheet; previously one of us would update the scores after every game.

## Tools Used to Solve the Problem: 
This program relied heavily on csv (for long-term data storage), defaultdict (for short-term data storage), BeautifulSoup (for web scraping), and input() (to collect user input from the command line). [Visual Studio Code](https://code.visualstudio.com/) was the IDE I used (and highly recommend!) to develop this program. 

## Learnings:
This project was an incredibly fun way to learn more about project development in terms of the iterative/incremental process (helping me to finally understand Agile). While assignments in class were quick 'one-offs', this project required more overall planning and thoughtfulness.

From this project I solidified my understanding of loops, git, defining/calling function, dictionaries, reading/writing csv files, collecting input from the command line, and *especially* debugging in an IDE.

Learning web scraping has been a goal of mine for a while, and was one of the most enjoyably frustrating parts of this project. I am definitely looking forward to exploring BeautifulSoup more, as I either enhance this program or dive into another personal project.

## Limitations:
While this project accomplishes the goal of creating a Python implementation of my friend group's **Snek Draft**, it does not go beyond the output that is currently in place. With the power of web scraping, it would be interesting to see more statistics and team metrics, such as team performance over time, division/league comparisons, and betting odds.

Currently, the draft is setup to require that it happens in one single instance. This means that while draft results are stored in a csv, the draft cannot be 'paused' and then resumed at a later point. While this reflects the current process amongst my friend group, I would address this limitation by adding logic for detecting a pre-existing partial draft potentially using/storing a draft round counter variable.

## Screenshots/Walkthrough:
Video walkthrough available here: https://youtu.be/Yrg6RowBKZc

GitHub repo located here: https://github.com/bwats2/CSCIE7-Final-Project

Screenshot of the Main Menu:![Image of the text-based main menu](mainmenu.jpg "Main Menu")

## Initialization/How-to-Use:
Initialize main.py from the command line (python main.py). Follow main menu and subsequent prompts. User input is entered directly into the command line.