import sqlite3
import pandas as pd
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
db_path = os.path.join(os.path.dirname(__file__), 'indo_spotify.db')

conn = sqlite3.connect(db_path)

# Load all normalized tables
artist_df = pd.read_csv(os.path.join(data_dir, 'artist.csv'))
artist_genre_df = pd.read_csv(os.path.join(data_dir, 'artist_genre.csv'))
album_df = pd.read_csv(os.path.join(data_dir, 'album.csv'))
album_artist_df = pd.read_csv(os.path.join(data_dir, 'album_artist.csv'))
track_df = pd.read_csv(os.path.join(data_dir, 'track.csv'))
track_artist_df = pd.read_csv(os.path.join(data_dir, 'track_artist.csv'))

artist_df.to_sql('artist', conn, if_exists='replace', index=False)
artist_genre_df.to_sql('artist_genre', conn, if_exists='replace', index=False)
album_df.to_sql('album', conn, if_exists='replace', index=False)
album_artist_df.to_sql('album_artist', conn, if_exists='replace', index=False)
track_df.to_sql('track', conn, if_exists='replace', index=False)
track_artist_df.to_sql('track_artist', conn, if_exists='replace', index=False)

conn.close()
print("All normalized tables loaded into the database successfully!")