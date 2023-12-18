import json
from main import get_song_features

f = open("data/ex_playlist_1.json")
data = json.load(f)
uris = set()
tracks = []
for track in data["tracks"]:
    if track["track_uri"] not in uris:
        uris.add(track["track_uri"])
        uri = track['track_uri'].split(":")[-1]
        song = get_song_features(uri)
        t = {
            "_op_type": "index",
            "_index": "index1",
            "artist_name": track["artist_name"],
            "track_uri": track["track_uri"],
            "artist_uri": track["artist_uri"],
            "track_name": track["track_name"],
            "album_uri": track["album_uri"],
            "duration_ms": track["duration_ms"],
            "album_name": track["album_name"],
            'danceability': song["danceability"],
            'energy': song['energy'],
            'key': song['key'],
            'loudness': song['loudness'],
            'mode': song['mode'],
            'speechiness': song['speechiness'],
            'acousticness': song['acousticness'],
            'instrumentalness': song['instrumentalness'],
            'liveness': song['liveness'],
            'valence': song['valence'],
            'tempo': song['tempo']
        }
        tracks.append(t)
final = json.dumps(tracks, indent=2)
file = open("data/ex_playlist_1_sanitized.json", "w")
file.write(final)
file.close()
