import asyncio
import discord
from discord.ext import commands
from utils import variables, functions, randomorg

class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_client = variables.voice_client
        self.voice_channel = self.bot.get_channel(variables.SAY_CHANNEL)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        try:
            self.voice_channel = self.bot.get_channel(variables.SAY_CHANNEL)
            self.voice_client = await voice_channel.connect()
        except:
            pass
        voice_client = self.voice_client
        if (member != self.bot.user):
            if (after.channel):
                if (after.channel.id == variables.SAY_CHANNEL):
                    await asyncio.sleep(0.5)
                    audio = randomorg.element(variables.FILES)
                    try:
                        voice_client.play(discord.FFmpegPCMAudio(f'voice\\{audio}'))
                    except discord.errors.ClientException:
                        functions.log(f'{member.nick if member.nick else member} не получит кик с канала.', 'y')
                    voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
                    voice_client.source.volume = 0.50
                    DURATION = functions.get_duration(f'voice\\{audio}')
                    await asyncio.sleep(DURATION)
                    await member.move_to(None)


    @commands.command(aliases = ['ресет', 'reset'])
    async def file_reset(self, ctx):
        functions.update_audio()
        await ctx.send(f'Можым слушоть {randomorg.element(variables.FILES)}, мой гаспадин')

def setup(bot):
    bot.add_cog(VoiceCog(bot))
