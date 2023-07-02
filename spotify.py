import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")
username = os.getenv("username")
playlist_id = os.getenv("playlist_id")
playlist_privacy = os.getenv("playlist_privacy")

scope = f"playlist-modify-{playlist_privacy}"  # or 'playlist-modify-private'

token = SpotifyOAuth(
    scope=scope,
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    username=username,
)

sp = spotipy.Spotify(auth_manager=token)


def get_current_songs():
    results = sp.playlist(playlist_id)
    songs = [item["track"]["id"] for item in results["tracks"]["items"]]
    return songs


def get_track_id(song_name, artist_name):
    query = f"track:{song_name} artist:{artist_name}"
    response = sp.search(query, type="track", limit=1)

    if not response["tracks"]["items"]:
        correct_song_name = song_name.replace("'", "").split(" (")[0]
        query = f"track:{correct_song_name} artist:{artist_name}"
        response = sp.search(query, type="track", limit=1)

    if response["tracks"]["items"]:
        return response["tracks"]["items"][0]["id"]
    else:
        print(f"No track found for {song_name} by {artist_name}")
        return None


# replace old playlist with new playlist
def update_playlist(song_ids):
    try:
        sp.playlist_replace_items(playlist_id, song_ids)
        print("Succesfully updated playlist")
        print(f"Find here: https://open.spotify.com/playlist/{playlist_id}")
    except Exception as e:
        print(e)
        print("Error updating playlist")


def print_song_from_trackid(track_id):
    track = sp.track(track_id)
    print(f"{track['name']} by {track['artists'][0]['name']}")
