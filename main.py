from apple import get_apple_music_playlist
from spotify import (
    get_track_id,
    update_playlist,
)


def main():
    apple_music_songs = get_apple_music_playlist()
    apple_song_ids = [get_track_id(song[0], song[1]) for song in apple_music_songs]
    # remove all None values from apple_song_ids
    apple_song_ids = [x for x in apple_song_ids if x is not None]
    # only keep 100 songs
    apple_song_ids = apple_song_ids[:50]
    update_playlist(apple_song_ids)


if __name__ == "__main__":
    main()
