import discord
import pickledb
from discord.ext import commands 

bot = commands.Bot(command_prefix = "ас")
db = pickledb.load('data.db', False)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='команду "асхелп"'))

@bot.event
async def on_message(message):
    channel = bot.get_channel(message.channel.id)
    if (message.author == "Гошасс" and message.content == "СУЙ"):
        await channel.send(file = discord.File('a1.jpg'))
        if (str(message.author) in db.getall()):
                tempvalue = db.get(str(message.author))
                tempvalue = int(tempvalue)
                tempvalue += 1
                db.set(str(message.author), str(tempvalue))
        elif (str(message.author) not in db.getall()):
            db.set(str(message.author), '1')


@bot.group(name = "догма")
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
            await ctx.send("Ну тут пока пусто.")
    elif (clan in ["а", "a", "f",]):
        if (_key == "девиз" or _key == "ltdbp"):
            await ctx.send("Прах ты, и в прах возвратишься!")
        elif (_key == 1):
            await ctx.send(file = discord.File('a1.jpg'))
            if (str(ctx.message.author) in db.getall()):
                tempvalue = db.get(str(ctx.message.author))
                tempvalue = int(tempvalue)
                tempvalue += 1
                db.set(str(ctx.message.author), str(tempvalue))
            elif (str(ctx.message.author) not in db.getall()):
                db.set(str(ctx.message.author), '1')

@truly.command(name = "сет")
async def setting(ctx):
    await ctx.send("Yess!")

@bot.command(name = "огурцы")
async def counting(ctx):
    output = ''
    for tempk in db.getall():
        tempv = db.get(tempk)
        output += tempk + " - " + tempv + ":cucumber:\n"
    await ctx.send(output)

@bot.command(name = "хелп")
async def helping(ctx):
    await ctx.send('>>> Привет!\nИспользуй "асхелп" для вызова этого сообщения еще раз.\n(а = ашены, р = русские)\n"асдогма клан число" - отправляет в чат фразу или картинку, которую флот взял за догму.\n"асдогма клан девиз" - отправляет девиз флота.')  


bot.run('NjcwNjkyOTAwNTkzNTk4NTMw.XjMD-A.PexcB1UaMP9tbr8UDBngY7oWJrM')
