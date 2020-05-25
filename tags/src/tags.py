import discord
from discord.ext import commands
from utils import functions, variables

class TagsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['тег', 'тэг', 'tag'])
    async def astag(self, ctx, user: discord.Member, *, args):

        eng = 'There\'s a tag on this user\'s mention already.'
        rus = 'На тег этого человека уже воспроизводится команда.'
        tchannel = self.bot.get_channel(692447840148127864)
        if (variables.tags.search(variables.SUI.id == user.id) == []):
            variables.tags.insert({'id' : user.id, 'message' : args})
            if (variables.recovering == False):
                await tchannel.send(f'астег {user.id} {args}')
        else:
            if (ctx.message.content.lower().startswith('as')):
                await ctx.send(eng)
            else:
                await ctx.send(rus)


    @commands.Cog.listener()
    async def on_message(self, message):

        for user in variables.tags.all():
            dmember = self.bot.get_user(user['id'])
            if (dmember in message.mentions):
                await message.channel.send(user['message'])

        Killant = self.bot.get_user(472853149137240064)
        if (Killant in message.mentions):
            await message.channel.send('```#КИЛЛ ВЕРНИСЬ В КОНОХУ```')


def setup(bot):
    bot.add_cog(TagsCog(bot))
