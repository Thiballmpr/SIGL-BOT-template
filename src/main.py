import os
import discord
from discord.member import Member
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 243792152012914700  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def admin(ctx, user: discord.Member):
    roles = ctx.guild.roles
    if not get(roles, name="Admin"):
        perms = discord.Permissions(manage_channels=True, kick_members=True, ban_members=True)
        ctx.guild.create_roles(name='Admin', colour=discord.Colour(0x0062ff), permissions=perms)
        ctx.send('Role created')
    await user.add_roles('Admin')

@bot.command()
async def mute(ctx, arg: discord.Member):
    await arg.edit(mute=True)

@bot.command()
async def ban(ctx, user: discord.Member):
    await user.ban()


token = os.getenv("DISCORD_TOKEN")
bot.run(token)  # Starts the bot