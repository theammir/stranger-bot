import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "u")
@bot.command
async def ping(ctx):
    ctx.send("Pong!")

bot.run('LFCOKZWih7k-KaWMJY5v0TiNDg-JXW6T')
