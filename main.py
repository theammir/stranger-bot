import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "ас")



@bot.event
async def on_message(message):
    channel_id = message.channel.id
    channel = bot.get_channel(channel_id)
    if (message.content == "асping"):
        await channel.send("Upong, " + str(message.author) + "!")
    elif (message.content == "асдогма а 1" or (message.author.name == "Гошасс" and message.content == "СУЙ")):
        await channel.send(file=discord.File('a1.jpg'))
    elif (message.content == "асдогма а девиз"):
        await channel.send("Прах ты, и в прах возвратишься!")
    elif (message.content == "асинвайт а"):
        if (str(message.author.roles[1]) == "Феникс"):
            await channel.send("https://discord.gg/sH9GjzP")
        else:
            await channel.send("Ты можешь поделиться инвайтом только своего клана.")
    elif (message.content == "асинвайт р"):
        if (str(message.author.roles[1]) == "Нефритовый воин"):
            await channel.send("https://discord.gg/T3EKbtc")
        else:
            await channel.send("Ты можешь поделиться инвайтом только своего клана.")

bot.run('NjcwNjkyOTAwNTkzNTk4NTMw.Xi8ckg.cSsBtA8xcNoWjHXodgJdV-tDV4Q')
