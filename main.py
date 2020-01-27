import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "u")

@bot.command
async def ping(ctx):
    await ctx.send("Pong!")

bot.run('NjcwNjkyOTAwNTkzNTk4NTMw.Xi8ckg.cSsBtA8xcNoWjHXodgJdV-tDV4Q')
