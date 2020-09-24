# 10_update_csv.py

# update the csv data previously downloaded
# do some simple data cleaning 

import pandas as pd
import os
from utility import create_folders

DIR_PROCESSED ='data/processed'

create_folders([DIR_PROCESSED])

df = pd.read_csv('data/hurricanes.csv')
print(df.info())

# df_sample = df.head(100)
# df_sample.to_csv(os.path.join(DIR_PROCESSED, 'sample.csv'), index=False)


# clean up column names
df.columns = df.columns.str.replace('"','').str.replace(' ', '')
print(df.columns)

# update original file
df.to_csv('hurricanes.csv', index=False)


# keep some columns 

df_sample = df[['Month', 'Average', '2013', '2014', '2015']]
df_sample.to_csv(os.path.join(DIR_PROCESSED, 'sample.csv'), index=False)
print(f"Sample File is saved at {os.path.join(DIR_PROCESSED, 'sample.csv')}")