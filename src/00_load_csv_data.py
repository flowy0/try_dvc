# objective:
# create a repo, write a script to load in a csv file and a few images,
# update the csv a couple times and commit the mods, then print the history of the csv.exit

# imports
import requests
import os
import pandas as pd
# import logging
from utility import create_folders


# load some data
# https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html

# maintain some variables
DIR_DATA = 'data'
csv_link = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hurricanes.csv'


def get_csv(csv_link=csv_link, file_name ='hurricanes.csv', dir_path=DIR_DATA):
    req = requests.get(csv_link)
    data = req.content
    output_file_path = os.path.join(dir_path, file_name)

    csv_file = open(output_file_path, 'wb')
    csv_file.write(data)
    csv_file.close()
    print(f'File is saved at {output_file_path}')


def get_sample_csv(file_path=os.path.join(DIR_DATA,'hurricanes.csv'), output_file='sample.csv'):
    df = pd.read_csv(file_path)

    df_sample = df.head(100)
    df_sample.to_csv(os.path.join(DIR_DATA, output_file), index=False)


if __name__ == "__main__": 
    #create some folders to store
    create_folders([DIR_DATA])
    #get a csv
    get_csv()
    get_sample_csv()
