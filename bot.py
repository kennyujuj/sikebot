import discord
from discord.ext import commands



intents = discord.Intents.default()
intents.members = True
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?',intents=intents)

@bot.event
async def on_ready():
    print("bot is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(977433749664985118)
    await channel.send(f'{member} join')
    print(f'{member}join')
    

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(977433749664985118)
    await channel.send(f'{member} fell in to the void')
    print(f'{member}leave')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run('MTAxOTI3MzQ1NzE2NDM1NzcwMw.GG2fmW.S_DQCgTtGn9LMiTZmgjvJqP8tbt_Wqt0QN9MKU')