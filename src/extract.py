import os
import requests
import json
from dotenv import load_dotenv

# Load credentials
load_dotenv('env', override=True)
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_access_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials'}
    resp = requests.post(url, headers=headers, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    return resp.json()['access_token']

def get_artist_info(artist_id, token):
    url = f'https://api.spotify.com/v1/artists/{artist_id}'
    headers = {'Authorization': f'Bearer {token}'}
    return requests.get(url, headers=headers).json()

def get_artist_albums(artist_id, token, limit=10, offset=0, market='ID'):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/albums'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'limit': limit, 'offset': offset, 'market': market}
    return requests.get(url, headers=headers, params=params).json()

def get_artist_top_tracks(artist_id, token, market='ID'):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'market': market}
    return requests.get(url, headers=headers, params=params).json()

if __name__ == '__main__':
    # List of artist IDs (example: Hindia, Lomba Sihir, Feast)
    ARTIST_IDS = [
        '51kyrUsAVqUBcoDEMFkX12',  # Hindia
        '6wD3vtAV0P3gWB9zLs7I4j',  # Lomba Sihir
        '7Gy1PxqrgsiqWF6JNYPHeB',  # Feast
    ]
    token = get_access_token()

    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_dir, exist_ok=True)

    for artist_id in ARTIST_IDS:
        artist_info = get_artist_info(artist_id, token)
        albums = get_artist_albums(artist_id, token)
        top_tracks = get_artist_top_tracks(artist_id, token)

        # Save data to JSON files per artist
        with open(os.path.join(data_dir, f'artist_{artist_id}.json'), 'w', encoding='utf-8') as f:
            json.dump(artist_info, f, ensure_ascii=False, indent=2)
        with open(os.path.join(data_dir, f'albums_{artist_id}.json'), 'w', encoding='utf-8') as f:
            json.dump(albums, f, ensure_ascii=False, indent=2)
        with open(os.path.join(data_dir, f'top_tracks_{artist_id}.json'), 'w', encoding='utf-8') as f:
            json.dump(top_tracks, f, ensure_ascii=False, indent=2)

        print(f'Data for artist {artist_id} saved successfully!')