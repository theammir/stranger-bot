import discord
from discord.ext import commands
from random import randint
from tinydb import TinyDB, Query

bot = commands.Bot(command_prefix = "ас")
db = TinyDB('data.json')
SUI = Query()
dictwithsui = []
suislist = []
nameslist = []
counter = 0

def isSorted(): # Returns True or False if the array is sorted or it isn't
    global counter
    counter = 0
    for element in suislist: # [-5, 5, -10, 1, 25]
        if (counter != len(suislist) - 1): # For no "index out of range" exception
            if (suislist[counter] < suislist[counter + 1]): # Comparing of two numbers
                return False
                break
            else:
                counter += 1
        elif (counter == len(suislist) - 1):
            return True

async def sort():
    for i in db.all():
        suislist.append(i['count'])
        nameslist.append(i['name'])
    if (len(db.all()) > 1):
        while (isSorted()):
            for i in range(0, len(suislist) - 1):
                if (temp[i] < temp[i + 1]):
                    suislist[i], suislist[i + 1] = suislist[1 + 1], suislist[i]
                    nameslist[i], nameslist[i + 1] = nameslist[i + 1], nameslist[i]
                else:
                    pass
    else:
        return False
    

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
            dictwithsui = db.search(SUI.name == str(message.author))
            if (dictwithsui == []):
                db.insert({'name' : str(message.author), 'count' : 1})
                dictwithsui = db.search(SUI.name == str(message.author))
                dictwithsui = dictwithsui[0]['count']
            else:
                dictwithsui = dictwithsui[0]['count']
                db.update({'count' : dictwithsui + 1}, SUI.name == str(message.author))
            await channel.send(file = discord.File('a1.jpg'))
    elif (cantent.startswith("Ъуъ") or cantent.startswith('ъуъ') or cantent.startswith('ъУъ') or cantent.startswith('ъуЪ') or cantent.startswith("ЪУЪ") or cantent.startswith('ЪуЪ') or cantent.startswith("ЪУъ") or cantent.startswith('ъУЪ') or cantent.startswith('iyi')
          or cantent.endswith('Ъуъ') or cantent.endswith('ъуъ') or cantent.endswith('ЪУЪ') or cantent.endswith('ъУъ') or cantent.endswith('ъуЪ') or cantent.endswith('ЪУъ') or cantent.endswith('ъУЪ') or cantent.endswith('ЪуЪ') or cantent.endswith('iyi')):
        if (autor[len(autor) - 4 : len(autor)] in ["5103", '6109', '4789', '8787']):
            dictwithsui = db.search(SUI.name == str(message.author))
            if (dictwithsui == []):
                db.insert({'name' : str(message.author), 'count' : 1})
                dictwithsui = db.search(SUI.name == str(message.author))
                dictwithsui = dictwithsui[0]['count']
            else:
                dictwithsui = dictwithsui[0]['count']
                db.update({'count' : dictwithsui + 1}, SUI.name == str(message.author))
        await channel.send(file = discord.File('a2.jpg'))
    elif (str(message.content) == "цвет пакажы"):
        while (1==1):
            await message.author.roles[len(message.author.roles) - 1].edit(colour = discord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255)), reason = None)
    await bot.process_commands(message)



@bot.command(name = 'каунт')
async def count(ctx):
    global suislist
    global nameslist
    if (await sort() == False):
        await ctx.send(nameslist[0] + ' сунул ' + str(suislist[0]) + ":cucumber:!")
    else:
        for i in range(0, len(suislist) - 1):
            speech += nameslist[i] + ' сунул ' + str(suislist[i]) + ':cucumber:!\n'
        try:
            await ctx.send(speech)
        except:
            await ctx.send('По видимому, база данных пуста :bigboom:\nНу, либо что-то опять в который раз пошло не так ;/')
    


@bot.group(aliases = ["догма", 'Догма', "Домга", "домга"])
async def truly(ctx, clan : str, _key : str):
    clan = clan.lower()
    _key = _key.lower()
    try:
        _key = int(_key)
    except:
        if (_key == "девиз" or _key == "ltdbp"):
            pass
        else:
            await ctx.send("Бот просит передавать в качестве второго аргумента функции тип данных integer.\nПроще говоря, нужно писать число после буквы клана, а не вот это ваше \"" + _key + "\".")
            return 1 / 0 # Command ending
    if (clan in ["р", "p", "h",]):
            await ctx.send("Союз распался в ~~1991~~ 2019.")
    elif (clan in ["а", "a", "f",]):
        if (_key == "девиз" or _key == "ltdbp"):
            await ctx.send("Прах ты, и в прах возвратишься!")
        elif (_key == 1):
            await ctx.send(file = discord.File('a1.jpg'))
        elif (_key == 2):
            await ctx.send(file = discord.File('a2.jpg'))


@truly.command(name = "сет")
async def setting(ctx):
    await ctx.send("Yess!")



@bot.command(name = "хелп")
async def helping(ctx):
    await ctx.send('>>> Привет!\nИспользуй "асхелп" для вызова этого сообщения еще раз.\n"асдогма а число" - отправляет в чат фразу или картинку, которую флот взял за догму.\n"асдогма а девиз" - отправляет девиз флота.\n"асптица @ник" - выдаёт роль кандидата. Работает только при наличии роли с правом выдачи кандидата.\n"аспогости @ник" выдаёт гостя кандидату, работает при наличии роли обучатора или иных руководящих ролей.')  


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




bot.run('NjcwNjkyOTAwNTkzNTk4NTMw.XkKF2w.h6r_sfTu50dFFugcQhhj5bcAAIY')
