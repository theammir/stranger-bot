from tinydb import TinyDB, Query
from os import listdir
from discord import VoiceClient

SUI = Query()
FILES = list(filter(lambda i: i.startswith('t') and i.endswith('.mp3'), listdir('voice')))
voice_client = None
recovering = False
db   = TinyDB('dogmas/data.json')
tags = TinyDB('tags/dbta.json')

SAY_CHANNEL      = 712265525140652052
DOGMAS_CHANNEL   = 685840409116540930
MENTIONS_CHANNEL = 692447840148127864

REQUIRED    = ['обучатор', 'совет флота', 'адмирал', 'вице адмирал', 'доверенный']
ADVENTURER  = 686634008444141618
ENSIGN      = 705497106273534034
GUEST       = 670719148699156511
