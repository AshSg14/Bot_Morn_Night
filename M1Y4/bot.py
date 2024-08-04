import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command('morn')
async def morn(ctx: commands.Context):
    lst = os.listdir('images')
    with open(f'images/morning.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command('night')
async def night(ctx: commands.Context):
    lst = os.listdir('images')
    with open(f'images/night.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run('')
