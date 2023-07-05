from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv

load_dotenv()
apple_playlist_url = os.getenv("apple_playlist_url")


def get_apple_music_playlist():
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # turn off outputs on console from webdriver
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # WebDriver Manager takes care of the rest
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get(apple_playlist_url)

    # get songs
    songListContainer = driver.find_elements_by_class_name("songs-list")
    # get elements from songListContainer with className 'svelte-1qne0gs'
    songList = songListContainer[0].find_elements_by_class_name("songs-list-row")
    songs = []
    for song in songList:
        songData = song.text.split("\n")
        songs.append((songData[0], songData[1]))
    if len(songs) == 0:
        RuntimeError("No songs found in playlist, please check your playlist url and try again")
    
    driver.quit()
    return songs
