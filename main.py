import discord
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix = "ас")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='команду "асхелп"'))

@bot.event
async def on_message(message):
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
    await ctx.send('>>> Привет!\nИспользуй "асхелп" для вызова этого сообщения еще раз.\n"асдогма а число" - отправляет в чат фразу или картинку, которую флот взял за догму.\n"асдогма а девиз" - отправляет девиз флота.\n"асптица @ник" - выдаёт роль кандидата. Работает только при наличии роли с правом выдачи кандидата.')  


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
        





bot.run('NjcwNjkyOTAwNTkzNTk4NTMw.Xj12Ew.27tDAS5PeBDBQ4On5KH2zb5NNRc')
