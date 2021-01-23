import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = '%')

@client.event
async def on_ready():
    print('Avengers Assembled.')

@client.event
async def on_memeber_join(member):
    print(f'{member} has been recruited to the Avengers!')

@client.command()
async def ping(ctx):
    await ctx.send("Reporting for duty!")

@client.command()
async def shield(ctx):
    await ctx.send("Shields up!")

@client.command()
async def spam(ctx, par):
    if par == '1':
        await ctx.send("Haha")
    elif par == '2':
        await ctx.send("oh no!")
    else:
        await ctx.send("lmao")

@client.command(pass_context=True)
#@commands.has_role("Developer")
async def role_adder(ctx, rolename):
    await ctx.send("adding role")
    author = ctx.message.author
    try:
        role = get(author.guild.roles, name=rolename)
        await author.add_roles(role)
        await ctx.send("role added")
    except:
        await ctx.send("an error has occured")

# @client.command()
# async def emotecheck(ctx, emname):
#     msg = ctx.send("React to this message!")
#     emote = get(ctx.message.guild.emojis, name=emname)
#     reaction = client.wait_for_reaction([emote], msg)
#     await client.send(f'You reacted with {reaction.emoji}')


client.run('ODAyNTk1MzE5NDM0MTgyNzA5.YAxhIw.6njS_-b8pYv8DEGgzB79kIEJaSE')
