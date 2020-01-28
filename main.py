import discord
# import pickledb
from discord.ext import commands

bot = commands.Bot(command_prefix = "ас")
#db = pickledb.load('db', False)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='команду "асхелп"'))


@bot.event
async def on_message(message):
    channel_id = message.channel.id
    channel = bot.get_channel(channel_id)
    if (message.content.lower() == "асping"):
        await channel.send("Upong, " + str(message.author) + "!")
    elif (message.content.lower() == "асдогма а 1" or (message.author.name == "Гошасс" and message.content == "СУЙ")):
       await channel.send(file=discord.File('a1.jpg'))
    elif (message.content.lower() == "асдогма а девиз"):
        await channel.send("Прах ты, и в прах возвратишься!")
    elif (message.content.lower() == "асинвайт а"):
        if (str(message.author.roles[1]) == "Феникс"):
            await channel.send("https://discord.gg/sH9GjzP")
        else:
            await channel.send("Ты можешь поделиться инвайтом только своего клана.")
    elif (message.content.lower() == "асинвайт р"):
        if (str(message.author.roles[1]) == "Нефритовый воин"):
            await channel.send("https://discord.gg/T3EKbtc")
        else:
            await channel.send("Ты можешь поделиться инвайтом только своего клана.")
    elif (message.content.lower() == "асхелп"):
        await channel.send('>>> Привет!\nИспользуй "асхелп" для вызова этого сообщения еще раз.\n(а = ашены, р = русские)\n"асдогма клан число" - отправляет в чат фразу или картинку, которую флот взял за догму.\n"асдогма клан девиз" - отправляет девиз флота.')


@bot.command(name = "хелп")
async def helping(ctx):
    await print("Хелп принят")


bot.run('NjcwNjkyOTAwNTkzNTk4NTMw.Xi8ckg.cSsBtA8xcNoWjHXodgJdV-tDV4Q')
