from discord.ext import commands
import discord
from utils import variables, functions, randomorg, tokens
import os

async def get_pre(bot, message):
    return ['сас', 'САС', 'Сас', 'сАС', 'саС',
            'ас', 'Ас', 'АС', 'аС',
            'ass', 'Ass', 'ASS', 'aSS', 'asS',
            'as', 'As', 'aS', 'AS',]

bot = commands.Bot(command_prefix = get_pre, case_insensitive = True)
functions.log('Обьект бота инициализирован.')

bot.remove_command('help')
functions.reset(variables.db)

@bot.event
async def on_ready():
    channel = bot.get_channel(693112638275584260)
    message = await channel.fetch_message(693112703492816898)
    ctx = await bot.get_context(message)

    await bot.change_presence(activity = discord.Game(name='"асхелп"/"ashelp"'))

    guild = bot.get_guild(671432722236964884)
    def changecolor(id, guild = guild):
        role = guild.get_role(id)
        colour = discord.Colour.from_rgb(randomorg.integer(0, 255), randomorg.integer(0, 255), randomorg.integer(0, 255))
        return role.edit(colour = colour)
    await changecolor(673966918281199616)
    await changecolor(685813138301780027)
    await changecolor(676388955985412116)
    await changecolor(676389164727402517)
    functions.log('Цвета ролей обновлены.')

    print()
    sum = 0
    for i in os.listdir():
        if ('.' not in i):
            if (i != 'utils' and i != 'Procfile'):
                try:
                    bot.load_extension(f'{i}.src.{i}')
                except:
                    pass
                length = functions.get_length(f"{i}/src/{i}.py")
                functions.log(f'({length} lines) {i} был загружен.', 'm', 'COG')
                sum += length
    sum += functions.get_length('main.py')
    for i in os.listdir('utils'):
        sum += functions.get_length(f'utils/{i}')
    bot.unload_extension('voice.src.voice')

    functions.log(f'Всего строк: {sum}.', 'm', 'LEN')
    print()

    # await recover(ctx = ctx)
    functions.log('Базы данных восстановлены.')

    functions.log('Бот готов к работе.')

@commands.is_owner()
@bot.command(aliases = ['лоад', 'load'])
async def cog_load(ctx, cog):
    try:
        bot.load_extension(f'{cog}.src.{cog}')
    except commands.errors.ExtensionAlreadyLoaded:
        await ctx.send(f'`{cog.upper()} is already loaded.`', delete_after = 5.0)
    length = functions.get_length(f"{cog}/src/{cog}.py")
    await ctx.send(f'`{cog.upper()} cog was loaded. ({length} lines)`')
    functions.log(f'({length} lines) {cog} был загружен.', 'm', 'COG')

@commands.is_owner()
@bot.command(aliases = ['анлоад', 'unload'])
async def cog_unload(ctx, cog):
    bot.unload_extension(f'{cog}.src.{cog}')
    length = functions.get_length(f"{cog}/src/{cog}.py")
    await ctx.send(f'`{cog.upper()} cog was unloaded. ({length} lines)`', delete_after = 5.0)
    functions.log(f'({length} lines) {cog} был отгружен.', 'm', 'COG')

@commands.is_owner()
@bot.command(aliases = ['релоад', 'reload'])
async def cog_reload(ctx, cog):
    bot.unload_extension(f'{cog}.src.{cog}')
    bot.load_extension(f'{cog}.src.{cog}')
    length = functions.get_length(f"{cog}/src/{cog}.py")
    await ctx.send(f'`{cog.upper()} cog was reloaded. ({length} lines)`', delete_after = 5.0)
    functions.log(f'({length} lines) {cog} был перезагружен.', 'm', 'COG')


@bot.command(name = 'рекавер', aliases = ['recover', 'rcv'])
async def recover(ctx):
    eng = ['Recover 2.0\nStatus: START',
            'Dogmas recovering is started.',
            'Recover 2.0\nStatus: END',
            'Dogmas recovering is ended.']
    rus = ['Рекавер 2.0\nСтадия: СТАРТ',
            'Начинается восстановление догм.',
            'Рекавер 2.0\nСтадия: END',
            '~~Вирусная база данных успешно обновлена~~']
    variables.db.purge()
    variables.tags.purge()
    channel = ctx.message.channel
    author = str(ctx.message.author)
    roles = ''
    variables.recovering = True
    for i in ctx.message.author.roles:
        roles += str(i)
    if ('Администратор догм' in roles):
        pass
    else:
        return
    assets = bot.get_channel(685840409116540930)
    astags = bot.get_channel(692447840148127864)
    functions.reset(variables.db)
    async with channel.typing():
        if (ctx.message.content.lower().startswith('as')):
            await channel.send(eng[0])
            await channel.send(eng[1])
        else:
            await channel.send(rus[0])
            await channel.send(rus[1])
    async for i in assets.history(limit = 1000):
        if not (i.content.lower().startswith('ассет')):
            await i.delete()
        else:
            key = i.content.split(' ')[1]
            content = tuple(i.content.split(' ')[2:])

            dogmas = bot.get_cog('DogmasCog')
            await dogmas.tset(ctx, key, *content)
    async for i in astags.history(limit = 1000):
        user = i.content.split(' ')[1]
        if (bot.get_user(int(user))):
            user = bot.get_user(int(user))
            args = ' '.join(i.content.split(' ')[2:])

            tags = bot.get_cog('TagsCog')
            await tags.astag(ctx, user = user, args = args)
        else:
            await i.delete()
            await bot.get_channel(685553321901293605).send(f'Асте\г был удалён. ({user.id}) - ({args})')
    recovering = False
    async with channel.typing():
        if (ctx.message.content.lower().startswith('as')):
            await channel.send(eng[2])
            await channel.send(eng[3])
        else:
            await channel.send(rus[2])
            await channel.send(rus[3])


@bot.command(name = 'ребут', aliases = ['reboot'])
async def reboot(reconnect = True):
    await bot.close()
    bot.run(tokens.ASTRANGER)


@bot.command(name = 'пьюрдж', aliases = ['purge'])
async def dbpurge(ctx):
    channel = ctx.message.channel
    roles = ''
    for role in ctx.message.author.roles:
        roles += str(role)
    roles = roles.lower()
    if ('креатор' not in roles):
        async with channel.typing():
            if not (ctx.message.content.lower().startswith('as')):
                await channel.send('**ДА КАК ТЫ ПОСМЕЛ, СМЕРТНЫЙ?!**')
            else:
                await channel.send('**HOW DARE YOU?!**')
        return
    else:
        variables.db.purge()
        variables.tags.purge()
        functions.log('Базы данных были очищены!', 'y')


functions.log('Инициализированы все необходимые команды.')
functions.log('Бот подготавливается к запуску.')
bot.run(tokens.ASTRANGER)
