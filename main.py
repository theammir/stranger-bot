import discord
from discord.ext import commands
from random import randint, choice
import requests as rq
from tinydb import TinyDB, Query

async def get_pre(bot, message):
  return ['ас', 'Ас', 'АС', 'аС']  # or a list, ["pre1","pre2"]

bot = commands.Bot(command_prefix = get_pre)

ASTRANGER = 'NjcwNjkyOTAwNTkzNTk4NTMw.Xl5srA.AIm-zDe-A6YvCElKQshQqoCkJ0c'
BSTRANGER = 'NjcyMTE1NzgyNDM5OTI3ODQw.Xl5sow.DU_HeHUNmRF0HoNfddiTQWKREnA'
BFTAE = 'Njc1Mzg5MDYwNjc5OTkxMzA4.Xl5snA.NkH8QucLvWbtil1hr-wKU0G6-dc'
db = TinyDB('data.json')
SUI = Query()
counter = 0
_key = ''
recovering = False
if (db.search(SUI.image == 'a1.jpg') == []):
    db.insert({'_key' : '1', 'image' : 'a1.jpg', 'message' : ''}) # СУЙ
    db.insert({'_key' : '2', 'image' : 'a2.jpg', 'message' : ''}) # ЪУЪ

@bot.event
async def on_ready():
    channel = bot.get_channel(671432725109932045)
    await bot.change_presence(activity=discord.Game(name='команду "асхелп"'))
    guild = bot.get_guild(671432722236964884)
    COLOURER = 673966918281199616
    SOVIET = 685813138301780027
    CREATOR = 676388955985412116
    ADMIN = 676389164727402517
    colour = discord.Colour.from_rgb(randint(0, 256), randint(0, 256), randint(0, 256))
    await guild.get_role(COLOURER).edit(colour = colour, reason = None)
    colour = discord.Colour.from_rgb(randint(0, 256), randint(0, 256), randint(0, 256))
    await guild.get_role(SOVIET).edit(colour = colour, reason = None)
    colour = discord.Colour.from_rgb(randint(0, 256), randint(0, 256), randint(0, 256))
    await guild.get_role(CREATOR).edit(colour = colour, reason = None)
    colour = discord.Colour.from_rgb(randint(0, 256), randint(0, 256), randint(0, 256))
    await guild.get_role(ADMIN).edit(colour = colour, reason = None)

    
@bot.event
async def on_message(message):
    channel = bot.get_channel(message.channel.id)
    autor = str(message.author)
    cantent = str(message.content)
    if (str(message.content).startswith('//')):
        _key = str(message.content)[2:]
        ctx = await bot.get_context(message)
        await dogme(ctx, clan = 'a', key = _key)
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
    


@bot.group(name = 'догма')
async def dogme(ctx, clan : str, key : str):
    _key = key
    dictionary = db.search(SUI._key == _key)
    try:
        img = dictionary[0]['image']
    except:
        pass
    if (dictionary != []):
        try:
            await ctx.send(dictionary[0]['message'])
        except:
            pass
        try:
            await ctx.send(file = discord.File(img))
        except:
            pass
    else:
        await ctx.send("Бот нифига не нашел")

@bot.command(name = 'рекавер')
async def recover(ctx):
    global recovering
    roles = ''
    recovering = True
    for role in ctx.message.author.roles:
        roles += str(role)
    if ('Администратор догм' not in roles):
        return
    channel = bot.get_channel(685840409116540930)
    await ctx.send('Начинаю восстановление догм.')
    async for msg in channel.history(limit = 500):
        try:
            if (str(msg.content) != 'Догма с таким ключом уже существует :teahah:'):
              content = str(msg.content).split(' ')
              content = content[1:]
              _key = content[0]
              content = content[1:]
              await tset(ctx, _key, content)
        except Exception as e:
            await ctx.send('Произошла ошибка при копироввании догмы!:')
            await ctx.send(str(e))
    await ctx.send('~~Вирусная база данных успешно обновлена!~~')
    recovering = False

@bot.command(name = 'сет')
async def tset(ctx, _key : str, *content):
    global recovering
    channel = bot.get_channel(685840409116540930)
    if (recovering == False):
        await channel.send(str(ctx.message.content))
    for i in _key:
        if (i in ['*', '/', '|', '\\',]):
            await ctx.send('Я запрещаю вам использовать спецсимволы!')
            return
    listContent = []
    for i in content:
        listContent.append(i)
    if (_key == '1' or _key == '2'):
        await ctx.send('Нельзя изменять изначальные догмы.')
        return
    for i in db.all():
        if (i['_key'] == _key):
            if (recovering == False):
                await ctx.send('Догма с таким ключом уже существует :teahah:')
                return
    listContent[0] = ' '.join(listContent[0])
    strContent = ' '.join(listContent)
    print(str(listContent))
    if (strContent.startswith('https://')):
        link = listContent[0]
        extention = '.png'
        if (link.endswith('.jpg') or link.endswith('.jpeg')):
            extention = '.jpg'
        elif (link.endswith('.png')):
            extention = '.png'
        message = ' '.join(listContent[1:])
        
        html = rq.get(link, stream = True)
        with open(f'a{_key}{extention}', 'bw') as f:
            for chunk in html.iter_content(8192):
                f.write(chunk)
        db.insert({'_key' : _key, 'message' : message, 'image' : f'a{_key}{extention}'})
    else:
        message = ' '.join(listContent)
        db.insert({'_key' : _key, 'message' : message})
            
@bot.command(name = 'лист')
async def dlist(ctx):
    allbase = db.all()
    for i in allbase:
        await ctx.send(f'Key: {i["_key"]}, Message: {i["message"]}')
    
@bot.command(aliases = ['радуга', 'лгбт'])
async def rainbow(ctx):
    randkey = choice(db.all())['_key']
    if (randkey == 'нсфв'):
        randkey = choice(db.all())['_key']
    dictionary = db.search(SUI._key == randkey)
    if (dictionary != []):
        try:
            await ctx.send(dictionary[0]['message'])
        except Exception as e:
            #await ctx.send(e)
            pass
        try:
            img = dictionary[0]['image']
            await ctx.send(file = discord.File(img))
        except Exception as e:
            pass

@bot.command('делит')
async def delete(ctx, _key):
    roles = ''
    for role in ctx.message.author.roles:
        roles += str(role)
    if ('Член ботского совета' in roles):
        db.remove(SUI._key == _key)
        async for i in bot.get_channel(685840409116540930).history(limit = 500):
            if (str(i.content).lower().startswith(f'ассет {_key}')):
                await i.delete()
                return




    
@bot.command(name = "хелп")
async def helping(ctx):
    await ctx.send('>>> Привет!\nИспользуй "асхелп" для вызова этого сообщения еще раз.\nЗа помощью или что-бы предложить что-то своё, обращайтесь в https://discord.gg/A4NETzF\n"асдогма а <число>" - отправляет в чат фразу или картинку, которую флот взял за догму.\n"асдогма а девиз" - отправляет девиз флота.\n"асптица <@ник>" - выдаёт роль кандидата. Работает только при наличии роли с правом выдачи кандидата.\n"аспогости <@ник>" выдаёт гостя кандидату, работает при наличии роли обучатора или иных руководящих ролей.\n"ассет <номер> <ссылка на картинку cdn.discordapp>(опционально) <текст>(опционально)" - при наличии одного из аргументов запоминает вашу собственную догму, которую можно воспроизвести.\n:stop_sign:"асрадуга" - выводит случайную догму из списка оных (осторожно, возможно наличие 18+ контента (nsfw).)')  


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




bot.run(BSTRANGER)
