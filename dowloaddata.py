import mlcroissant as mlc
import pandas as pd
import os

croissant_dataset = mlc.Dataset('https://www.kaggle.com/datasets/shivamb/netflix-shows/croissant/download')
record_sets = croissant_dataset.metadata.record_sets
record_set_df = pd.DataFrame(croissant_dataset.records(record_set=record_sets[0].uuid))

print(record_set_df.head())
print("Saving CSV to current directory:", os.getcwd())

record_set_df.to_csv('netflix_titles.csv', index=False)
