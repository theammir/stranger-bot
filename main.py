import discord
from discord.ext import commands
from random import randint, choice
import requests as rq
from bs4 import BeautifulSoup as bs
import shutil
from tinydb import TinyDB, Query

async def get_pre(bot, message):
  return ['ас', 'Ас', 'АС', 'аС']

bot = commands.Bot(command_prefix = get_pre, case_insensetive = True)
ASTRANGER = 'NjcwNjkyOTAwNTkzNTk4NTMw.Xl5srA.AIm-zDe-A6YvCElKQshQqoCkJ0c'
BSTRANGER = 'NjcyMTE1NzgyNDM5OTI3ODQw.Xl5sow.DU_HeHUNmRF0HoNfddiTQWKREnA'
BFTAE     = 'Njc1Mzg5MDYwNjc5OTkxMzA4.Xl5snA.NkH8QucLvWbtil1hr-wKU0G6-dc'
db = TinyDB('data.json')
tags = TinyDB('dbta.json')
SUI = Query()
counter = 0
_key = ''
recovering = False
if (db.search(SUI.image == 'a1.jpg') == []):
    db.insert({'_key' : '1', 'image' : 'a1.jpg', 'message' : ''}) # СУЙ
    db.insert({'_key' : '2', 'image' : 'a2.jpg', 'message' : ''}) # ЪУЪ


@bot.event
async def on_ready():
    channel = bot.get_channel(693112638275584260)
    message = await channel.fetch_message(693112703492816898)
    ctx = await bot.get_context(message)
    await bot.change_presence(activity = discord.Game(name='команду "асхелп"'))
    guild = bot.get_guild(671432722236964884)
    COLOURER = 673966918281199616
    SOVIET = 685813138301780027
    CREATOR = 676388955985412116
    ADMIN = 676389164727402517
    colour = discord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    await guild.get_role(COLOURER).edit(colour = colour, reason = None)
    colour = discord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    await guild.get_role(SOVIET).edit(colour = colour, reason = None)
    colour = discord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    await guild.get_role(CREATOR).edit(colour = colour, reason = None)
    colour = discord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    await guild.get_role(ADMIN).edit(colour = colour, reason = None)
    await recover(ctx = ctx)


@bot.event
async def on_message(message):
    channel = message.channel
    autor = str(message.author)
    cantent = str(message.content)
    Killant = bot.get_user(472853149137240064)
    if (str(message.content).startswith('//')):
        _key = str(message.content)[2:]
        ctx = await bot.get_context(message)
        await dogme(ctx, clan = 'a', key = _key)
    #if (str(message.author) == "Гошасс#8787" and str(message.content) == "СУЙ" or str(message.author) == "ΤχεΑμμιΡ#6109"and message.content == "СУЙ"):
    for user in tags.all():
        dmember = bot.get_user(user['id'])
        if (dmember in message.mentions):
            await channel.send(' '.join(user['message']))
    if (str(message.content) == "СУЙ"):
          if (autor[len(autor) - 4 : len(autor)] in ["8787", "6109"]):
              async with channel.typing():
                  await channel.send(file = discord.File('a1.jpg'))
    elif (Killant in message.mentions):
        await channel.send('```#КИЛЛ ВЕРНИСЬ В КОНОХУ```')
    elif (cantent.lower().startswith(('ъуъ', 'ъyъ', 'ъγъ', 'iyi', 'iуi', 'iγi')) or cantent.lower().endswith(('ъуъ', 'ъyъ', 'ъγъ', 'iyi', 'iуi', 'iγi'))):
        if (autor[len(autor) - 4 : len(autor)] in ["5103", '6109', '4789', '8787']):
            await channel.send(file = discord.File('a2.jpg'))
    elif (str(message.content) == "цвет пакажы"):
        while (1==1):
            await message.author.roles[len(message.author.roles) - 1].edit(colour = discord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255)), reason = None)
    await bot.process_commands(message)


@bot.group(name = 'догма')
async def dogme(ctx, clan : str, key : str):
    channel = ctx.message.channel
    _key = key
    dictionary = db.search(SUI._key == _key)
    try:
        img = dictionary[0]['image']
    except:
        pass
    async with channel.typing():
        if (dictionary != []):
            try:
                await channel.send(dictionary[0]['message'])
            except:
                pass
            try:
                await channel.send(file = discord.File(img))
            except:
                pass
        else:
            await channel.send("Бот нифига не нашел")


@bot.command(aliases = ['тег', 'тэг'])
async def astag(ctx, user, *, args):
    global recovering
    tchannel = bot.get_channel(692447840148127864)
    try:
        user = int(user)
    except:
        if (tags.search(SUI.id == user.id) == []):
            tags.insert({'id' : user.id, 'message' : args})
            if (recovering == False):
                await tchannel.send(f'астег {str(user.id)} {args}')
        else:
            await ctx.send('На тег этого человека уже воспроизводится команда.')
            return
    else:
        if (tags.search(SUI.id == user) == []):
            tags.insert({'id' : user, 'message' : args})
            if (recovering == False):
                await tchannel.send(str(ctx.message.content))
        else:
            await ctx.send('На тег этого человека уже воспроизводится команда.')
            return



@bot.command(name = 'рекавер')
async def recover(ctx):
    db.purge()
    tags.purge()
    channel = ctx.message.channel
    global recovering
    roles = ''
    recovering = True
    for role in ctx.message.author.roles:
        roles += str(role)
    if ('Администратор догм' not in roles):
        return
    assets = bot.get_channel(685840409116540930)
    astags = bot.get_channel(692447840148127864)
    async with channel.typing():
        await channel.send('Рекавер 2.0\nСтадия: СТАРТ')
        await channel.send('Начинается восстановления догм.')
    async for i in assets.history():
        _key = i.content.split(' ')[1]
        content = tuple(i.content.split(' ')[2:])
        await tset(ctx, _key, *content)
    async for i in astags.history():
        user = i.content.split(' ')[1]
        args = i.content.split(' ')[2:]
        await astag(ctx, user = user, args = args)
    recovering = False
    async with channel.typing():
        await channel.send('Рекавер 2.0\nСтадия: END')
        await channel.send('~~Вирусная база данных успешно обновлена~~')


@bot.command(name = 'сет')
async def tset(ctx, _key : str, *content):
    global recovering
    achannel = bot.get_channel(685840409116540930)
    channel = ctx.message.channel
    if (recovering == False):
        async with achannel.typing():
            await achannel.send(str(ctx.message.content))
    for i in _key:
        if (i in ['*', '/', '|', '\\',]):
            async with channel.typing():
                await channel.send('Я запрещаю вам использовать спецсимволы!')
            return
    listContent = []
    for i in content:
        listContent.append(i)
    if (_key == '1' or _key == '2'):
        async with channel.typing():
            await channel.send('Нельзя изменять изначальные догмы.')
        return
    for i in db.all():
        if (i['_key'] == _key):
            if (recovering == False):
                async with channel.typing():
                    await channel.send('Догма с таким ключом уже существует :teahah:')
                return
    listContent[0] = ''.join(listContent[0])
    strContent = ' '.join(listContent)
    if (strContent.startswith('https://')):
        link = listContent[0]
        link = link.replace(' ', '')
        link = str(link.split('?')[0])
        extention = ''
        if (link.endswith('.jpg') or link.endswith('.jpeg')):
            extention = '.jpg'
        elif (link.endswith('.png')):
            extention = '.png'
        elif (link.endswith('.gif')):
            extention = '.gif'
        else:
            print(link.replace(' ', '_'))
        message = ' '.join(listContent[1:])

        response = rq.get(link, stream = True)
        with open(f'a{_key}{extention}', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        db.insert({'_key' : _key, 'image' : f'a{_key}{extention}', 'message' : message})
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


@bot.command(name = "хелп")
async def helping(ctx):
    channel = ctx.message.channel
    async with channel.typing():
        await channel.send('Привет!')
        embed = discord.Embed(
            title = 'Список команд',
            colour = discord.Colour.from_rgb(153, 95, 199),
            type = 'rich',
            description = 'Бота A STRANGER:',
        )
        embed.add_field(name = 'Команда помощи', value = '"асхелп" для вызова этого сообщения еще раз')
        embed.add_field(name = 'Сервер Странника', value = 'За помощью или что-бы предложить что-то своё, обращайтесь в https://discord.gg/A4NETzF')
        embed.add_field(name = 'Команда догм', value = '"асдогма а <ключ>" - отправляет в чат фразу или картинку, которую флот взял за догму.')
        embed.add_field(name = 'Девизы', value = '"асдогма а девиз" - пишет девиз флота.')
        embed.add_field(name = 'Сптичить гостя', value = '"асптица <@ник>" выдаёт роль кандидата человеку. Работает при наличии роли обучатора.')
        embed.add_field(name = 'Выдать гостя обратно', value = '"аспогости <@ник>" выдаёт гостя кандидату, работает при наличии роли обучатора или иных руководящих ролей.')
        embed.add_field(name = 'Своя догма', value = '"ассет <номер> <ссылка на картинку cdn.discordapp>(опционально) <текст>(опционально)" - при наличии одного из аргументов запоминает вашу собственную догму, которую можно воспроизвести.')
        embed.add_field(name = ':stop_sign:Воля случая', value = '"асрадуга" - выводит случайную догму из списка оных (осторожно, возможно наличие 18+ контента (nsfw).)')
        embed.add_field(name = ':x:Удаление догм', value = '"асделит <ключ>" удаляет догму. Недоступно для обычного пользователя.')
        embed.add_field(name = ':x:Сломались догмы?', value = 'За помощью к Айсу/Гоше можно обратиться всегда за исключением того, если на сервере нет Гоши по каким-то причинам')
        embed.add_field(name = 'Коронавирус', value = '"асинфа <country>(опционально) - статистика по заражению коронавирусом."')
        await channel.send(embed = embed)


@bot.command(name = "птица")
async def fetch(ctx, person : discord.Member):
    channel = ctx.message.channel
    if (str(ctx.message.author) == str(person)):
        async with channel.typing():
            await channel.send("Вы не можете давать роль сами себе или у вас нет соответствующего разрешения")
        pass
    guild = bot.get_guild(person.guild.id)
    roles = ''
    for element in ctx.message.author.roles:
        roles += str(element)
    if ('обучатор' not in roles):
        async with channel.typing():
            await channel.send('Нужно быть обучатором, что-бы пользоваться этой командой')
    else:
        await person.add_roles(guild.get_role(670649392398729270), reason=None)
        await person.remove_roles(guild.get_role(670719148699156511), reason=None)


@bot.command(name = 'ребут')
async def reboot(reconnect = True):
    await bot.close()
    bot.run(ASTRANGER)


@bot.command(name = 'погости')
async def guesting(ctx, person : discord.Member):
    channel = ctx.message.channel
    if (str(ctx.message.author) == str(person)):
        async with channel.typing():
            await channel.send('Вы не можете изменять роли самому себе.')
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
            async with channel.typing():
                await channel.send('Вы не имеете права на изменение ролей этого человека.')
            break


@bot.command(name = 'пьюрдж')
async def dbpurge(ctx):
    channel = ctx.message.channel
    roles = ''
    for role in ctx.message.author.roles:
        roles += role
    roles = roles.lower()
    if ('креатор' not in roles):
        async with channel.typing():
            await channel.send('ДА КАК ТЫ ПОСМЕЛ, СМЕРТНЫЙ?!')
        return
    else:
        db.purge()

@bot.command(name = 'инфа')
async def coronainfo(ctx, country = ''):
    if (country == ''):
        r = rq.get('https://www.worldometers.info/coronavirus/')
    else:
        r = rq.get('https://www.worldometers.info/coronavirus/country/' + country.lower())
    html = bs(r.content, 'html.parser')
    span = html.select('.container > .row > .col-md-8 > .content-inner > #maincounter-wrap > h1')
    count = html.select('.container > .row > .col-md-8 > .content-inner > #maincounter-wrap > .maincounter-number > span')
    for i in range(3):
        await ctx.send(f'{span[i].text} {count[i].text}')

bot.run(ASTRANGER)
