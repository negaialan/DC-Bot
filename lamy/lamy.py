import os
import discord
from discord.ext import commands
import json
import random
from discord.ext.commands import Bot

with open('C:\\discord bot\\lamy\\setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='?',intents=intents)

@bot.event
async def on_ready():
    print("on_ready")
    channel = bot.get_channel(int(jdata['lamybot']))
    await channel.send("こんらみ!!!")

for filename in os.listdir('C:\\discord bot\\lamy\\command'):
    if filename.endswith('.py'):
        bot.load_extension(f'command.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])