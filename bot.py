import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import time

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

@client.command()
async def emotecheck(ctx, emname, rolename):
    msg = await ctx.send(f"React to this message with {emname}")
    await msg.add_reaction(emname)
    emote = get(ctx.message.guild.emojis, name=emname)
    def check(reaction, user):
        return reaction.message == msg and reaction.emoji == emname
    t_end = time.time() + 15
    while time.time() < t_end:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=t_end-time.time(), check=check)
        except asyncio.TimeoutError:
            await ctx.send('Reacting period has ended.')
        else:
            await ctx.send("adding role")
            try:
                role = get(user.guild.roles, name=rolename)
                await user.add_roles(role)
                await ctx.send("role added")
            except:
                await ctx.send("an error has occured")
    #await ctx.send('Reacting period has ended.')


client.run('token here')
