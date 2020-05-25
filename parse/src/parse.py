import discord
from discord.ext import commands

import requests as rq
from bs4 import BeautifulSoup as bs

class ParseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'инфа', aliases = ['infa', 'info'])
    async def coronainfo(self, ctx, country = ''):
        if (country == ''):
            r = rq.get('https://www.worldometers.info/coronavirus/')
        else:
            r = rq.get('https://www.worldometers.info/coronavirus/country/' + country.lower())
        html = bs(r.content, 'html.parser')
        span = html.select('.content-inner > #maincounter-wrap > h1')
        count = html.select('.content-inner > #maincounter-wrap > .maincounter-number > span')
        for i in range(3):
            await ctx.send(f'{span[i].text} {count[i].text}')


    @commands.command(name = 'kickstart', aliases = ['кикстарт', 'кикстрат', 'кикстартер', 'кикстратер', 'kickstarter'])
    async def kickstart(self, ctx):
        pledged = '$51,318'
        outof = '$20,000'
        backers = '555'
        intpledg = pledged.replace('$', '').replace(',', '')
        average = int(intpledg) / int(backers)
        if not (ctx.message.content.lower().startswith('as')):
            await ctx.send(f'Внесено {pledged} из {outof}.\nВнесли {backers} человек.\nСредний внос: ${average}.')
        else:
            await ctx.send(f'Now pledged {pledged} out of {outof}.\nBackers: {backers}\nAverage payment: ${average}.')


def setup(bot):
    bot.add_cog(ParseCog(bot))
