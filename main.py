import dotenv
import chesster
import os
from dotenv import load_dotenv, find_dotenv


if __name__ == '__main__':
    
    load_dotenv(find_dotenv())

    chesster = chesster.Bot()
    chesster.run(os.environ.get('botToken'))