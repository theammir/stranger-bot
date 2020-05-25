from tinydb import TinyDB, Query
from os import listdir
from discord import VoiceClient

SUI = Query()
SAY_CHANNEL = 712265525140652052
FILES = list(filter(lambda i: i.startswith('t') and i.endswith('.mp3'), listdir('voice')))
voice_client = None
recovering = False
db   = TinyDB('dogmas/data.json')
tags = TinyDB('tags/dbta.json')
