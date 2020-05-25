import discord
from discord.ext import commands

class ServerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'погости', aliases = ['guest'])
    async def guesting(ctx, person : discord.Member):

        rus = ['Вы не можете изменять роли самому себе.',
                'Вы не имеете права на изменение ролей этого человека.']
        eng = ['You can\'t edit your own roles.',
                'You can\'t edit roles of this member.']
        isrus = ctx.message.content.lower().startswith('as')
        channel = ctx.message.channel
        if (str(ctx.message.author) == str(person)):
            async with channel.typing():
                if (isrus):
                    await channel.send(rus[0])
                else:
                    await channel.send(eng[0])
            return
        guild = self.bot.get_guild(person.guild.id)
        roles = ''
        required_roles = ['обучатор', 'совет флота', 'адмирал', 'вице адмирал', 'доверенный']
        for element in ctx.message.author.roles:
            roles += str(element)
        roles = roles.lower()
        for element in required_roles:
            if (element in roles):
                await person.remove_roles(guild.get_role(686634008444141618), reason = None)
                await person.remove_roles(guild.get_role(705497106273534034), reason = None)
                await person.add_roles(guild.get_role(670719148699156511), reason = None)
                return
            else:
                async with channel.typing():
                    if (isrus):
                        await channel.send(rus[1])
                    else:
                        await channel.send(eng[1])
                return


    @commands.command(name = "птица", aliases = ['rookh', 'bird', 'ptitsa'])
    async def fetch(ctx, person : discord.Member):
        rus = ['Вы не можете давать роль сами себе.',
                'Вам нужна роль обучатора для использования этой команды.']
        eng = ['You can\'t give a role to you.',
                'Your need Обучатор role to use this command.']
        isrus = ctx.message.content.lower().startswith('as')
        channel = ctx.message.channel
        if (str(ctx.message.author) == str(person)):
            async with channel.typing():
                if (isrus):
                    await channel.send(rus[0])
                else:
                    await channel.send(eng[0])
            return
        guild = person.guild
        roles = ''
        for element in ctx.message.author.roles:
            roles += str(element)
        if ('обучатор' not in roles):
            async with channel.typing():
                if (isrus):
                    await channel.send(rus[1])
                else:
                    await channel.send(eng[1])
        else:
            await person.remove_roles(guild.get_role(686634008444141618), reason = None)
            await person.add_roles(guild.get_role(705497106273534034), reason = None)
            await person.remove_roles(guild.get_role(670719148699156511), reason = None)


def setup(bot):
    bot.add_cog(ServerCog(bot))
