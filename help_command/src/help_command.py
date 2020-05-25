import discord
from discord.ext import commands

class HelpCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "хелп", aliases = ['help', 'helping'])
    async def help(self, ctx):

        owner = self.bot.get_user(343001477133893632)
        eng = True if ctx.message.content.lower().startswith('as') else False
        channel = ctx.message.channel
        async with channel.typing():
            if not eng:
                await channel.send('Привет!')
                embed = discord.Embed(
                    title = 'Список команд',
                    colour = discord.Colour.from_rgb(153, 95, 199),
                    type = 'rich',
                    description = 'Бота A STRANGER:',
                )
                embed.add_field(name = 'Команда помощи', value = '"асхелп" для вызова этого сообщения еще раз')
                embed.add_field(name = 'Сервер Странника', value = 'За помощью или что-бы предложить что-то своё, обращайтесь в https://discord.gg/A4NETzF')
                embed.add_field(name = 'Команда догм', value = '"асдогма а <ключ>" ("//ключ") - отправляет в чат фразу или картинку, которую флот взял за догму.')
                embed.add_field(name = 'Девизы', value = '"асдогма а девиз" - пишет девиз флота.')
                embed.add_field(name = 'Сптичить гостя', value = '"асптица <@ник>" выдаёт роль кандидата человеку. Работает при наличии роли обучатора.')
                embed.add_field(name = 'Выдать гостя обратно', value = '"аспогости <@ник>" выдаёт гостя кандидату, работает при наличии роли обучатора или иных руководящих ролей.')
                embed.add_field(name = 'Своя догма', value = '"ассет <номер> <ссылка на картинку cdn.discordapp>(опционально) <текст>(опционально)" - при наличии одного из аргументов запоминает вашу собственную догму, которую можно воспроизвести.')
                embed.add_field(name = ':stop_sign:Воля случая', value = '"асрадуга" - выводит случайную догму из списка оных (осторожно, возможно наличие 18+ контента (nsfw).)')
                embed.add_field(name = ':x:Удаление догм', value = '"асделит <ключ>" удаляет догму. Недоступно для обычного пользователя.')
                embed.add_field(name = ':x:Сломались догмы?', value = 'За помощью к Айсу/Меззикусу можно обратиться всегда ~~за исключением того, если на сервере нет Гоши по каким-то причинам~~')
                embed.add_field(name = 'Сообщение при тэге', value = '"астег <пользователь> <сообщение>" - выдаёт сообщение при теге пользователя.')
                embed.add_field(name = 'Коронавирус', value = '"асинфа <country>(опционально) - статистика по заражению коронавирусом."')
                embed.add_field(name = 'Кикстартерская кампания', value = '"аскикстарт" показывает статистику прошлой кампании Pixel Starships на Kickstarter.')
                embed.set_footer(text = f'Автор: {owner}, все права занетканы и задолблены.', icon_url = owner.avatar_url)
            else:
                await channel.send('Hi! ;3')
                embed = discord.Embed(
                    title = 'A STRANGER bot',
                    colour = discord.Colour.from_rgb(153, 95, 199),
                    type = 'rich',
                    description = 'Command list',
                )
                embed.add_field(name = 'Help command', value = '"ashelp" to call this message again.')
                embed.add_field(name = 'A Stranger\'s Discord Server', value = 'For help or to offer something - https://discord.gg/A4NETzF')
                embed.add_field(name = 'Dogmas command', value = '"asdogma a <key>" ("//key") - sends a message or a picture the fleet has taken as a dogma.')
                embed.add_field(name = 'Mottos', value = '"asdogma a motto" - sends fleet motto.')
                embed.add_field(name = 'Make guest a bird', value = '"asbird <@mention>" gives a role of bird. Works only in presence of Обучатор role.')
                embed.add_field(name = 'Make bird a guest... yeah', value = '"asguest <@mention>" gives a role of guest. Works only in presence of Обучатор or other valuable roles.')
                embed.add_field(name = 'Your own dogma', value = '"asset <key> <picture link cdn.discordapp>(optional) <text>(optional)" - in the presence of one of the arguments, saves your dogma that can be sent by "asdogma a" or "//key"')
                embed.add_field(name = ':stop_sign:Will of chance', value = '"asrainbow" sends a random dogma. Be careful, NSFW ahead.')
                embed.add_field(name = ':x:Dogma deletion', value = '"asdelete <key>" deletes a dogma. Can\'t be used by regular user.')
                embed.add_field(name = ':x:Dogmas are broken?', value = 'Contact 『❄』I¢e Void『❄』#6609 or ΤχεΑμμιΡ#6109 for help.')
                embed.add_field(name = 'Mention message', value = '"astag <@mention or id> <message>" sends a message on user\'s mention.')
                embed.add_field(name = 'Coronavirus', value = '"asinfo <country>(optional)" - coronavirus cases statistics.')
                embed.add_field(name = 'Kickstarter company', value = '"askickstart" shows Pixel Starships Kickstarter end statistics.')
                embed.set_footer(text = f'Author: {owner}, all rights notted and beat.', icon_url = owner.avatar_url)
            await channel.send(embed = embed)


def setup(bot):
    bot.add_cog(HelpCommandCog(bot))
