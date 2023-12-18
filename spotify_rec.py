import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

credential = SpotifyClientCredentials(client_id='432aa7da4d9f438eb6f802fa5ef1aa7f', client_secret='1d23c394dfba42ca90e719b8a3945072')
sp = spotipy.Spotify(client_credentials_manager=credential)

results = sp.search(q='XO Tour Life lil uzi vert', type='track', limit=1)
id = results['tracks']['items'][0]['id']
features = sp.audio_features(id)[0]
similar_songs = sp.recommendations(seed_tracks=[id], target_danceability=features['danceability'], 
                                    target_energy=features['energy'], target_key=features['key'], 
                                    target_loudness=features['loudness'], target_mode=features['mode'], 
                                    target_speechiness=features['speechiness'], target_acousticness=features['acousticness'], 
                                    target_instrumentalness=features['instrumentalness'], target_liveness=features['liveness'], 
                                    target_valence=features['valence'], target_tempo=features['tempo'])
print('Songs similar to', ['name'])
for i, track in enumerate(similar_songs['tracks']):
    print(i+1, track['name'], '-', track['artists'][0]['name'])
