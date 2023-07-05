# check if .env file exists
import os
from generator import make_env
from main import main
from dotenv import load_dotenv

overwrite_env = False
if os.path.exists('.env'):
    set_env = input("Do you want to run Apple To Spotify with same settings as last time? (Y/n): ")
    if set_env == 'Y':
        overwrite_env = False
    else:
        overwrite_env = True
else:
    overwrite_env = True

if overwrite_env:
    make_env()

# clear terminal window
os.system('cls' if os.name == 'nt' else 'clear')
print("**********************************************")
main()