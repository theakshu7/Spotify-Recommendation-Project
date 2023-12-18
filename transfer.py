import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your own credentials
SPOTIPY_CLIENT_ID = '2f6ef674af204ec6ab3020c95cc5ca67'
SPOTIPY_CLIENT_SECRET = 'fb6a812038f24227ab48664be45ef569'
SPOTIPY_REDIRECT_URI = 'https://www.google.com/maps'

# Function to authenticate with Spotify API
def authenticate_spotify():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                     client_secret=SPOTIPY_CLIENT_SECRET,
                                                     redirect_uri=SPOTIPY_REDIRECT_URI,
                                                     scope='playlist-modify-private playlist-modify-public user-library-read user-library-modify'))

# Function to add songs to Liked Songs
def add_songs_to_liked(songs, sp):
    for song in songs:
        query = f"{song['name']} {song['artist']}"
        results = sp.search(q=query, type='track', limit=1)

        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.current_user_saved_tracks_add(tracks=[track_uri])
            print(f"Added {query} to Liked Songs.")
        else:
            print(f"Couldn't find {query} on Spotify.")

    print("Finished adding songs to Liked Songs.")

# Function to read songs from a file
def read_songs_from_file(file_path):
    songs = []
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header line
        for line in lines:
            data = line.strip().split('\t')
            song = {
                "name": data[0],
                "artist": data[1],
            }
            songs.append(song)
    return songs

# Main function
def main():
    # Replace 'your_file_path' with the path to your file
    file_path = 'test'

    # Read songs from the file
    songs = read_songs_from_file(file_path)

    # Authenticate with Spotify API
    sp = authenticate_spotify()

    # Add songs to Liked Songs
    add_songs_to_liked(songs, sp)

if __name__ == "__main__":
    main()
