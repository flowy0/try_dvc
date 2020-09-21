# objective:
# create a repo, write a script to load in a csv file and a few images,
# update the csv a couple times and commit the mods, then print the history of the csv.

# imports
import requests
import os
# load some data
# https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html

# maintain some variables
DIR_DATA = 'data'
csv_link = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hurricanes.csv'

req = requests.get(csv_link)
data = req.content

# not working yet 
output_file_path = os.path.join(DIR_DATA,"hurricanes.csv")
print(output_file_path)
csv_file = open(output_file_path, 'wb')
csv_file.write(data)
csv_file.close()