import asyncio
import discord
from discord.ext import commands
from sys import path
path.insert(1, '../../')
from utils import randomorg
from utils import variables
from utils.variables import db
path.pop(1)

import requests as rq
import shutil

class DogmasCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = 'догма', aliases = ['dogma', 'dogme'])
    async def dogme(self, ctx, clan: str, key: str):

        channel = ctx.message.channel
        key = key
        dictionary = db.search(variables.SUI.key == key)
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


    @commands.command(name = 'сет', aliases = ['set'])
    async def tset(self, ctx, key : str, *content):

        eng = ['You can\'t use such symbols.',
                'You can\'t edit original dogmas.',
                'A dogma with such key is already exists. :teahah:']
        rus = ['Я запрещаю вам использовать спецсимволы!',
                'Нельзя изменять изначальные догмы.',
                'Догма с таким ключом уже существует. :teahah:',]
        achannel = self.bot.get_channel(685840409116540930)
        channel = ctx.message.channel
        if (variables.recovering == False):
            async with achannel.typing():
                await achannel.send(str(ctx.message.content))
        for i in key:
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
        if (key == '1' or key == '2'):
            async with channel.typing():
                if (ctx.message.content.lower().startswith('as')):
                    await channel.send(eng[1])
                else:
                    await channel.send(rus[1])
            return
        for i in db.all():
            if (i['key'] == key):
                if (variables.recovering == False):
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
            with open(f'dogmas\\images\\a{key}{extention}', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            db.insert({'key' : key, 'image' : f'dogmas\\images\\a{key}{extention}', 'message' : message})
        else:
            message = ' '.join(listContent)
            db.insert({'key' : key, 'message' : message})


    @commands.command(name = 'rainbow', aliases = ['радуга', 'лгбт', 'lgbt', 'lgbtq', 'rnbw'])
    async def rainbow(self, ctx):

        randkey = randomorg.element(db.all())['key']
        dictionary = db.search(variables.SUI.key == randkey)
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


    @commands.command('делит', aliases = ['delete'])
    async def delete(self, ctx, key):

        roles = ''
        for role in ctx.message.author.roles:
            roles += str(role)
        if ('Член ботского совета' in roles):
            db.remove(SUI.key == key)
            async for i in self.bot.get_channel(685840409116540930).history(limit = 500):
                if (str(i.content).lower().startswith(f'ассет {key}')):
                    await i.delete()
        else:
            await ctx.send('Неимеиш права!1!!адинадин1ъъъъъ' if ctx.message.content.lower().startswith('ас') else 'You don\' have permission to do such things.')


    @commands.command(name = 'лист', aliases = ['list'])
    async def dlist(self, ctx, page : int = 1):

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
                title       = f'СПИСОК ДОГМ ({PAGE + 1}/{PAGES - 1})',
                description = f'Страница {PAGE + 1}',
                color       = discord.Colour.from_rgb(153, 95, 199)
            )
            for i in range(5):
                i += PAGE * PAGE_ELS
                fieldname = ''
                fieldvalue = ''
                if (allbase[i]['message'] != ''):
                    if (len(allbase[i]['key']) < 255):
                        fieldname = allbase[i]["key"]
                    else:
                        msg = allbase[i]['key']
                        fieldname = msg[:len(msg) - (len(msg) - 100) - 5 - len(allbase[i]["key"])] + '...'
                else:
                    fieldname = f'{allbase[i]["key"]} : `EMPTY`'

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
                reaction, user = await self.bot.wait_for('reaction_add', timeout = 30.0, check = lambda reaction, user: user == REQUESTED_BY and str(reaction.emoji) == '⏭️')
            except asyncio.TimeoutError:
                await sent.delete()
                return


    @commands.Cog.listener()
    async def on_message(self, message):
        if (str(message.content).startswith('//')):
            key = str(message.content).split(' ')[0][2:]
            ctx = await self.bot.get_context(message)
            await self.dogme(ctx, clan = 'a', key = key)


def setup(bot):
    bot.add_cog(DogmasCog(bot))
