import pandas as pd
from sqlalchemy import create_engine

# Load CSV into DataFrame
df = pd.read_csv('./netflix_titles.csv')

# Connect to your PostgreSQL database
engine = create_engine('postgresql://postgres@localhost:5432/test')

# Write data into SQL table (replace 'netflix_titles' with your table name)
df.to_sql('netflix_titles', engine, if_exists='replace', index=False)

print("Data inserted successfully!")
