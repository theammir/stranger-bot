import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "u")

@bot.event
async def on_message(message):
    channel_id = message.channel.id
    channel = bot.get_channel(channel_id)
    if (message.content == "uping"):
        await channel.send("Upong, " + str(message.author) + "!")

bot.run('NjcwNjkyOTAwNTkzNTk4NTMw.Xi8ckg.cSsBtA8xcNoWjHXodgJdV-tDV4Q')
