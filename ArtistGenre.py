import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

credential = SpotifyClientCredentials(client_id='cb039f3ac3804e99b1275c8f8555f3c6',
                                      client_secret='b7407a6fc72341d5b5d8f8f56dba37f6')
sp = spotipy.Spotify(client_credentials_manager=credential)

f = open("data/spotify_songs.json")
c = open("data/spotify_songs_genre.json")
data = json.load(f)
print(len(data))
tracks = json.load(c)
last = 30000
for i, song in enumerate(data):
    if i <= last:
        continue
    try:
        genre = sp.search(song["track_artist"], 1, 0, "artist")['artists']['items'][0]['genres']
    except:
        genre = []
    song["genre"] = genre
    tracks.append(song)
    if i % 100 == 0:
        print(i)
    if i % 5000 == 0 and i > 0:
        print(i)
        break

final = json.dumps(tracks, indent=2)
file = open("data/spotify_songs_genre.json", "w")
file.write(final)
file.close()
