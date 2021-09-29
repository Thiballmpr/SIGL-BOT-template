import os
from discord import guild, message, user
import discord
from discord.abc import User
from dotenv import load_dotenv
from discord.ext import commands
import mute

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
async def admin(ctx, arg):
    roles = ctx.guild
    if not roles.has_role(name="Admin"):
        ctx.guild.create_roles(name='Admin', colour=discord.Colour(0x0062ff))
        perms = discord.Permissions(manage_channels=True, kick_members=True, ban_members=True)
        ctx.guild.edit
    ctx.add_roles(arg, 'Admin')


token = os.getenv("DISCORD_TOKEN")
bot.run(token)  # Starts the bot