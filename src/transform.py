import pandas as pd
import json
import os
import glob

def transform_data():
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

    # --- Transform artist info & genres ---
    artist_rows = []
    genre_set = set()
    artist_genre_rows = []
    for file in glob.glob(os.path.join(data_dir, 'artist_*.json')):
        with open(file, 'r', encoding='utf-8') as f:
            artist_info = json.load(f)
        artist_rows.append({
            'artist_id': artist_info['id'],
            'name': artist_info['name'],
            'followers_total': artist_info['followers']['total'],
            'popularity': artist_info['popularity'],
            'spotify_url': artist_info['external_urls']['spotify']
        })
        for genre in artist_info.get('genres', []):
            genre_set.add(genre)
            artist_genre_rows.append({
                'artist_id': artist_info['id'],
                'genre': genre
            })
    artist_df = pd.DataFrame(artist_rows)
    artist_genre_df = pd.DataFrame(artist_genre_rows)

    # --- Transform albums & album_artist ---
    albums_rows = []
    album_artist_rows = []
    for file in glob.glob(os.path.join(data_dir, 'albums_*.json')):
        artist_id = os.path.basename(file).replace('albums_', '').replace('.json', '')
        with open(file, 'r', encoding='utf-8') as f:
            albums = json.load(f)
        for album in albums.get('items', []):
            image_url = max(album['images'], key=lambda x: x['height'])['url'] if album.get('images') else None
            albums_rows.append({
                'album_id': album['id'],
                'album_name': album['name'],
                'album_type': album.get('album_type'),
                'album_group': album.get('album_group'),
                'total_tracks': album.get('total_tracks'),
                'release_date': album.get('release_date'),
                'spotify_url': album['external_urls']['spotify'],
                'image_url': image_url
            })
            for a in album.get('artists', []):
                album_artist_rows.append({
                    'album_id': album['id'],
                    'artist_id': a['id']
                })
    albums_df = pd.DataFrame(albums_rows)
    album_artist_df = pd.DataFrame(album_artist_rows)

    # --- Transform top tracks & track_artist ---
    tracks_rows = []
    track_artist_rows = []
    for file in glob.glob(os.path.join(data_dir, 'top_tracks_*.json')):
        artist_id = os.path.basename(file).replace('top_tracks_', '').replace('.json', '')
        with open(file, 'r', encoding='utf-8') as f:
            top_tracks = json.load(f)
        for track in top_tracks.get('tracks', []):
            album = track['album']
            tracks_rows.append({
                'track_id': track['id'],
                'track_name': track['name'],
                'album_id': album['id'],
                'duration_ms': track.get('duration_ms'),
                'popularity': track.get('popularity'),
                'explicit': track.get('explicit'),
                'spotify_url': track['external_urls']['spotify']
            })
            for a in track.get('artists', []):
                track_artist_rows.append({
                    'track_id': track['id'],
                    'artist_id': a['id']
                })
    tracks_df = pd.DataFrame(tracks_rows)
    track_artist_df = pd.DataFrame(track_artist_rows)

    # --- Save to CSV ---
    artist_df.to_csv(os.path.join(data_dir, 'artist.csv'), index=False)
    artist_genre_df.to_csv(os.path.join(data_dir, 'artist_genre.csv'), index=False)
    albums_df.to_csv(os.path.join(data_dir, 'album.csv'), index=False)
    album_artist_df.to_csv(os.path.join(data_dir, 'album_artist.csv'), index=False)
    tracks_df.to_csv(os.path.join(data_dir, 'track.csv'), index=False)
    track_artist_df.to_csv(os.path.join(data_dir, 'track_artist.csv'), index=False)

    print('Data transformed, normalized, and saved successfully!')

if __name__ == "__main__":
    transform_data()