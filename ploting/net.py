import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


nf = pd.read_csv('../datasets/netflix_data.csv')

# get the movie only

movie = nf[nf['type'] == 'Movie']
movie_col_subset = movie[['title', 'country', 'genre', 'release_year', 'duration']]

fig = plt.figure(figsize=(12, 8))

col = []

for lab, row in movie_col_subset.iterrows():
    genre = row['genre']

    if genre == 'Children':
        col.append('blue')
    elif genre == 'Documentaries':
        col.append('yellow')
    elif genre == 'Stand-Up':
        col.append('green')
    else:
        col.append('black')

plt.scatter(movie_col_subset['release_year'], movie_col_subset['duration'], c=col)

plt.show()
