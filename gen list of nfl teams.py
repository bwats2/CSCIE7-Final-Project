import csv

team_list = []
# Open csv file
with open('data 2019 CSV.csv') as csvfile:
    # Skip first line (headers)
    csvfile.readline()
    # Use delimiter to parse data columns
    readCSV = csv.reader(csvfile, delimiter=',')
    # Iterate over rows
    for row in readCSV:
        # Read second column of data
        x = row[1]
        # Check that valid zipcode
        team_list.append(x)

print(sorted(team_list))