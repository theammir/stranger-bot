import discord
from discord.ext import commands
from random import randint
import requests as rq
from tinydb import TinyDB, Query
ASTRANGER = 'NjcwNjkyOTAwNTkzNTk4NTMw.Xl5srA.AIm-zDe-A6YvCElKQshQqoCkJ0c'
BSTRANGER = 'NjcyMTE1NzgyNDM5OTI3ODQw.Xl5sow.DU_HeHUNmRF0HoNfddiTQWKREnA'
BFTAE = 'Njc1Mzg5MDYwNjc5OTkxMzA4.Xl5snA.NkH8QucLvWbtil1hr-wKU0G6-dc'
bot = commands.Bot(command_prefix = "ас")
db = TinyDB('data.json')
SUI = Query()
dictwithsui = []
suislist = []
nameslist = []
counter = 0
_key = ''
if (db.search(SUI.image == 'a1.jpg') == []):
    db.insert({'_key' : '1', 'image' : 'a1.jpg', 'message' : ''}) # СУЙ
    db.insert({'_key' : '2', 'image' : 'a2.jpg', 'message' : ''}) # ЪУЪ

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='команду "асхелп"'))

@bot.event
async def on_message(message):
    global dictwithsui
    channel = bot.get_channel(message.channel.id)
    autor = str(message.author)
    cantent = str(message.content)
    
    #if (str(message.author) == "Гошасс#8787" and str(message.content) == "СУЙ" or str(message.author) == "ΤχεΑμμιΡ#6109"and message.content == "СУЙ"):
    if (str(message.content) == "СУЙ"):
        if (autor[len(autor) - 4 : len(autor)] in ["8787", "6109"]):
            await channel.send(file = discord.File('a1.jpg'))
    elif (cantent.startswith("Ъуъ") or cantent.startswith('ъуъ') or cantent.startswith('ъУъ') or cantent.startswith('ъуЪ') or cantent.startswith("ЪУЪ") or cantent.startswith('ЪуЪ') or cantent.startswith("ЪУъ") or cantent.startswith('ъУЪ') or cantent.startswith('iyi')
          or cantent.endswith('Ъуъ') or cantent.endswith('ъуъ') or cantent.endswith('ЪУЪ') or cantent.endswith('ъУъ') or cantent.endswith('ъуЪ') or cantent.endswith('ЪУъ') or cantent.endswith('ъУЪ') or cantent.endswith('ЪуЪ') or cantent.endswith('iyi')):
        if (autor[len(autor) - 4 : len(autor)] in ["5103", '6109', '4789', '8787']):
            await channel.send(file = discord.File('a2.jpg'))
    elif (str(message.content) == "цвет пакажы"):
        while (1==1):
            await message.author.roles[len(message.author.roles) - 1].edit(colour = discord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255)), reason = None)
    await bot.process_commands(message)
    


@bot.command(name = 'догма')
async def dogme(ctx, clan : str, key : str):
    _key = key
    if (clan.lower() in ('a', 'а', 'ф', 'f',)):
        if (_key.lower() == 'девиз'):
            await ctx.send('Прах ты, и в прах возвратишься!')
        else:
            dictionary = db.search(SUI._key == _key)
            try:
                img = dictionary[0]['image']
            except:
                pass
            if (dictionary != []):
                try:
                    await ctx.send(dictionary[0]['message'])
                except:
                    try:
                        await ctx.send(file = discord.File(img))
                    except:
                        pass
            else:
                await ctx.send("Бот нифига не нашел")
    elif (clan.lower() in ['р', 'p', 'з', 'h']):
        await ctx.send("Союз распался в ~~1991~~ 2019.")


@bot.command(name = 'сет')
async def sett(ctx, key : str, *, args = []):
    _key = key
    if (key == '1' or key == '2'):
        await ctx.send("Изначальные догмы не трогать!")
        return
    for i in db.all():
        if (i['_key'] == key):
            await ctx.send('Догма под таким номером уже существует.')
            return
    message = ''.join(args)
    if (message.startswith('https://')):
        link = message.split(' ')[0]
        message = ' '.join(message.split(' ')[1:])
        html = rq.get(link, stream = True)

        with open(f'a{_key}.png', 'bw') as f:
            for chunk in html.iter_content(8192):
                f.write(chunk)
        db.insert({'_key' : _key, 'message' : message, 'image' : f'a{_key}.png'})
    else:
        db.insert({'_key' : _key, 'message' : message})
            



@bot.command(name = "хелп")
async def helping(ctx):
    await ctx.send('>>> Привет!\nИспользуй "асхелп" для вызова этого сообщения еще раз.\nЗа помощью или что-бы предложить что-то своё, обращайтесь в https://discord.gg/A4NETzF\n"асдогма а <число>" - отправляет в чат фразу или картинку, которую флот взял за догму.\n"асдогма а девиз" - отправляет девиз флота.\n"асптица <@ник>" - выдаёт роль кандидата. Работает только при наличии роли с правом выдачи кандидата.\n"аспогости <@ник>" выдаёт гостя кандидату, работает при наличии роли обучатора или иных руководящих ролей.\n"ассет <номер> <ссылка на картинку cdn.discordapp>(опционально) <текст>(опционально)" - при наличии одного из аргументов запоминает вашу собственную догму, которую можно воспроизвести.')  


@bot.command(name = "птица")
async def fetch(ctx, person : discord.Member):
    if (str(ctx.message.author) == str(person)):
        await ctx.send("Вы не можете давать роль сами себе или у вас нет соответствующего разрешения")
        pass
    guild = bot.get_guild(person.guild.id)
    roles = ''
    for element in ctx.message.author.roles:
        roles += str(element)
    if ('обучатор' not in roles):
        await ctx.send('Нужно быть обучатором, что-бы пользоваться этой командой')
    else:
        await person.add_roles(guild.get_role(670649392398729270), reason=None)
        await person.remove_roles(guild.get_role(670719148699156511), reason=None)
        

@bot.command(name = 'ребут')
async def reboot(reconnect = True):
    await bot.close()
    while (bot.is_closed()):
        await bot.connect()

@bot.command(name = 'погости')
async def guesting(ctx, person : discord.Member):
    if (str(ctx.message.author) == str(person)):
        await ctx.send('Вы не можете изменять роли самому себе.')
        pass
    guild = bot.get_guild(person.guild.id)
    roles = ''
    required_roles = ['обучатор', 'совет флота', 'адмирал', 'вице адмирал', 'доверенный']
    for element in ctx.message.author.roles:
        roles += str(element)
    roles = roles.lower()
    for element in required_roles:
        if (element in roles):
            await person.remove_roles(guild.get_role(670649392398729270), reason = None)
            await person.add_roles(guild.get_role(670719148699156511), reason = None)
        else:
            await ctx.send('Вы не имеете права на изменение ролей этого человека.')
            break




bot.run(ASTRANGER)
