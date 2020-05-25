from utils import variables
from colorama import *
from mutagen.mp3 import MP3
from tinydb import TinyDB

init()

def log(message, code = 'g', tag = None):
    COLORS = {'g' : Fore.GREEN, 'y' : Fore.YELLOW, 'r' : Fore.RED,
              'c' : Fore.CYAN,  'm' : Fore.MAGENTA}

    if (COLORS.get(code)):
        print(f'[{COLORS[code]}ASTRANGER{Style.RESET_ALL}{" " + tag if tag else ""}] {message}')

def get_duration(file):
    audio = MP3(file)
    DURATION = audio.info.length
    return DURATION

def reset(db):
    SUI = variables.SUI
    if (db.search(SUI.key == '1') == []):
        db.insert({'key' : '1', 'image' : 'a1.jpg', 'message' : ''}) # СУЙ
        db.insert({'key' : '2', 'image' : 'a2.jpg', 'message' : ''}) # ЪУЪ
        log('Основные догмы восстановлены.')

def update_audio():
    variables.FILES = list(filter(lambda i: i.startswith('t') and i.endswith('.mp3'), listdir('../voice')))

def get_length(file):
    if ('__pycache__' not in file and '.' in file):
        with open(file, 'r', encoding = 'utf-8') as f:
            return len(list(filter(lambda i: i not in ['\n', ''], f.readlines())))
    else:
        return 0
