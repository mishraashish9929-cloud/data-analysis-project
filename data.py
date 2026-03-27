import pandas as pd
import numpy as np

df = pd.read_csv("netflix_titles.csv")
df.head()

# Handle Missing Values
df.isnull().sum()

df['country'].fillna("Unknown",inplace=True)
df['director'].fillna("Unknown",inplace=True)
df['cast'].fillna("Unknown",inplace=True)
df['date_added'].fillna("Unknown",inplace=True)
df['rating'].fillna("NOT RATED",inplace=True)
df['duration'].fillna("Duration Not Available",inplace=True)

# Convert Date column
df['date_added']=pd.to_datetime(df['date_added'],errors='coerce')
df['release_year']=df['date_added'].dt.year
df['listed_in']=df['listed_in'].str.split(',')
df['cast']==df['cast'].str.split(',')

Movies_vs_tvshows =df['type'].value_counts()
print(Movies_vs_tvshows)
Content_growth_over_time=df['release_year'].value_counts().sort_index()
Top_countries=df['country'].value_counts().head(10)
popular_genres=df.explode('listed_in')['listed_in'].value_counts().head(10)
rating_distribution=df['rating'].value_counts()
df.to_csv("cleaned_netflix_data.csv",index=False)

