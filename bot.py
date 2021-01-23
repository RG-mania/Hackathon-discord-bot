import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '%')

@client.event
async def on_ready():
    print('Avengers Assembled.')

client.run('ODAyNTk1MzE5NDM0MTgyNzA5.YAxhIw.Q27CxTnZMyfzMvrs902Eq0jhPak')
