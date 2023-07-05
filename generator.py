import os

def make_env():
    apple_playlist_url = input("Enter your Apple Music Playlist URL: ")
    client_id = input("Enter your Spotify Application Client ID: ")
    client_secret = input("Enter your Spotify Application Client Secret: ")
    redirect_uri = 'http://localhost:8080'
    user_id_url = input("Enter the url for your spotify profile: ")
    user_id = user_id_url.split('/')[-1]
    playlist_id_url = input("Enter the url for your spotify playlist: ")
    playlist_id = playlist_id_url.split('/')[-1]
    playlist_privacy = input("Enter the privacy of your playlist (public/private): ")

    with open('.env', 'w') as writeObj:
        writeObj.write(f'apple_playlist_url={apple_playlist_url}\n')
        writeObj.write(f'client_id={client_id}\n')
        writeObj.write(f'client_secret={client_secret}\n')
        writeObj.write(f'redirect_uri={redirect_uri}\n')
        writeObj.write(f'user_id={user_id}\n')
        writeObj.write(f'playlist_id={playlist_id}\n')
        writeObj.write(f'playlist_privacy={playlist_privacy}\n')

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("**********************************************")
    print("Welcome to Apple To Spotify Generator")
    print("Lets get some details about your playlist\n\n")
    print("**********************************************")
    make_env()
    