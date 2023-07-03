# Apple Music to Spotify Playlist Converter

This Python project fetches a list of songs from an Apple Music playlist and updates a Spotify playlist with the same set of songs. It uses `selenium` for web scraping, `webdriver_manager` to manage the ChromeDriver, `spotipy` to interact with Spotify's Web API, and `python-dotenv` to handle environment variables.

## File Structure
The project has the following python files:
1. `main.py`: The driver file where the main execution happens.
2. `apple.py`: Contains the function to fetch songs from an Apple Music playlist.
3. `spotify.py`: Contains functions to interact with Spotify Web API to fetch song IDs, and update a Spotify playlist.
4. `generator.py`: Setup script which takes user inputs to create the `.env` file necessary for execution.

A `requirements.txt` file is also included which contains the necessary dependencies for the project. 

A `.env` file (not included in the repository for security reasons) is used to store necessary environment variables.

## Setup

#### Requirements
* Python 3.x
* pip

To run this project, follow these steps:

1. Clone this repository to your local machine.

```sh
git clone https://github.com/peterrwilson99/AppleToSpotify
```

2. Install the required dependencies.
```sh
pip install -r requirements.txt
```

3. Environment Setup

This project requires some environment variables which are stored in a `.env` file. This file is not included in the repository for security reasons. To make setup easier, there is a Python script called `generator.py` which will guide you through the process of creating this .env file.

To run the setup script, use the following command:

```sh
python3 generator.py
```

The script will prompt you to enter:

- Your Apple Music Playlist URL
- Your Spotify Application Client ID
- Your Spotify Application Client Secret
- The URL for your Spotify profile
- The URL for your Spotify playlist you want to clone the songs to
- The privacy of your playlist (public/private)

After entering all the information, the script will create the .env file with all the necessary environment variables.

The .env file should look something like this:

```env
apple_playlist_url=https://music.apple.com/us/playlist/mixtape/pl.u-JPAZZZ7tGlWKEZ
client_id=YOUR_SPOTIFY_CLIENT_ID
client_secret=YOUR_SPOTIFY_CLIENT_SECRET
redirect_uri=YOUR_SPOTIFY_REDIRECT_URI
user_id=YOUR_SPOTIFY_USERID
playlist_id=YOUR_SPOTIFY_PLAYLIST_ID
playlist_privacy=public
```

4. Run the program.
```sh
python main.py
```

## Functionality
The program works as follows:

1. Using Selenium and ChromeDriver, it fetches the list of songs from the Apple Music Playlist provided in .env.
2. It then converts the song names and artist names fetched into track IDs using the Spotify Web API.
3. It then updates the provided Spotify playlist with these track IDs.


Please note, due to song availability and naming differences between Apple Music and Spotify, some songs might not get transferred.

Happy listening!                                                                                                                                    