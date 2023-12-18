import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

credential = SpotifyClientCredentials(client_id='432aa7da4d9f438eb6f802fa5ef1aa7f', client_secret='1d23c394dfba42ca90e719b8a3945072')
sp = spotipy.Spotify(client_credentials_manager=credential)

results = sp.search(q='Die for you', type='track', limit=1)

id = results['tracks']['items'][0]['id']
data = sp.track(id)
artist_id = data['artists'][0]['id']
artist_data = sp.artist(artist_id)
print('Name:', data['name'])
print('Artist:', data['artists'][0]['name'])
print('Album:', data['album']['name'])
print('Release Date:', data['album']['release_date'])
print('Popularity:', data['popularity'])
print('Genre:', artist_data['genres'])

features = sp.audio_features(id)[0]
print('Danceability:', features['danceability'])
print('Energy:', features['energy'])
print('Key:', features['key'])
print('Loudness:', features['loudness'])
print('Mode:', features['mode'])
print('Speechiness:', features['speechiness'])
print('Acousticness:', features['acousticness'])
print('Instrumentalness:', features['instrumentalness'])
print('Liveness:', features['liveness'])
print('Valence:', features['valence'])
print('Tempo:', features['tempo'])
print('Duration (ms):', features['duration_ms'])

def get_song_features(id):
    return sp.audio_features(id)[0]

def get_artist_genres(id):
    data = sp.track(id)
    artist_id = data['artists'][0]['id']
    artist_data = sp.artist(artist_id)
    return artist_data['genres']