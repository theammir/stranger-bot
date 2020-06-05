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
        required_roles = variables.REQUIRED
        for element in ctx.message.author.roles:
            roles += str(element)
        roles = roles.lower()
        for element in required_roles:
            if (element in roles):
                if (variables.ADVANTURER):
                    await person.remove_roles(guild.get_role(variables.ADVANTURER), reason = None)
                await person.remove_roles(guild.get_role(variables.ENSIGN), reason = None)
                await person.add_roles(guild.get_role(variables.GUEST), reason = None)
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
        required_roles = variables.REQUIRED
        for element in ctx.message.author.roles:
            roles += str(element)
        roles = roles.lower()
        for element in required_roles:
            if (element not in roles):
                async with channel.typing():
                    if (isrus):
                        await channel.send(rus[1])
                    else:
                        await channel.send(eng[1])
                    return
        if (variables.ADVANTURER):
            await person.remove_roles(guild.get_role(686634008444141618), reason = None)
        await person.add_roles(guild.get_role(variables.ENSIGN), reason = None)
        await person.remove_roles(guild.get_role(variables.GUEST), reason = None)


def setup(bot):
    bot.add_cog(ServerCog(bot))
