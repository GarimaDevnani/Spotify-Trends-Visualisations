#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:26:15 2022

@author: mojojojo
"""

import altair as alt
alt.data_transformers.disable_max_rows()

import pandas as pd

spotify_data = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv')

## DATA CLEANING

# Choosing and renaming columns
chosen_cols = ['track_name', 'track_artist', 'track_popularity',
               'track_album_release_date', 'playlist_genre', 
               'danceability', 'energy', 'loudness', 'acousticness', 
               'instrumentalness', 'duration_ms']
df = spotify_data[chosen_cols]
df = df.rename(
    {'track_popularity': 'popularity', 
     'track_artist': 'artist', 
     'track_album_release_date': 'release_date', 
     'playlist_genre': 'genre', 
     }, 
    axis=1
)

df = df.dropna() # dropping NA or null values
df.drop_duplicates(subset='track_name', keep=False, inplace=True) # dropping duplicate rows

#Adding information
df['duration_min'] = round(df['duration_ms']/60000, 2) # converting milliseconds to minute
df['release_year'] = df['release_date'].str[:4] # derive year from release date

df = df.drop('duration_ms', 1)
df = df.drop('release_date', 1)