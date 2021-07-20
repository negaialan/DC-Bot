import discord
from discord.ext import commands
from core.classes import Cog_Extension

class omeagr(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == '老婆':
            await msg.channel.send('醒')

def setup(bot):
    bot.add_cog(omeagr(bot))