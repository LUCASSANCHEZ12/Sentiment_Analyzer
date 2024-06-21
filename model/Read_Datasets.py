import os
import pandas as pd

directory = '.\\Datasets\\Steam reviews\\game_rvw_csvs'  # Name of the datasets directory
absolute_path = os.path.abspath(directory)

# Creating an empty dataframe
df_result = pd.DataFrame()

voted = True
# Iterating all the .csv files
for archivo in os.listdir(absolute_path):
    if archivo.endswith('.csv'):
        # Reading the csv file
        complete_path = os.path.join(absolute_path, archivo)
        df = pd.read_csv(complete_path)
        # only 1 million data
        if len(df_result) > 500000:
          voted = False
        elif len(df_result) > 1000000:
          break
        # Adding the voted_up column to the dataframe
        # and concatenating to the df_result
        df_filtered = df[df['voted_up'].astype(bool) == voted]

        df_result = pd.concat([df_result, df_filtered[['review','voted_up']]], ignore_index=True)

print(df_result.head())

df_result.to_csv('./dataset_training.csv', index=False)