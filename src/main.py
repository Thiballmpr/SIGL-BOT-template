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
        await ctx.guild.create_role(name='Admin', colour=discord.Colour(0x0062ff), permissions=perms)
    role = get(ctx.guild.roles, name="Admin")
    await user.add_roles(role)

@bot.command()
async def mute(ctx, arg: discord.Member):
    await arg.edit(mute=True)

@bot.command()
async def ban(ctx, user: discord.Member):
    await user.ban()


        
@bot.command(aliases=['x']) #command acceptor
async def xkcd(ctx,num=None,**kwargs): 
    """Posts the XKCD of the given number, if no number is given, posts the latest."""
    await ctx.channel.send(embed = await getcomic(ctx, num))

async def getcomic(ctx,num=None): #async func to get comic
    if num is None:
        num = 2
    async with bot.session.get(f'https://xkcd.com/{num}/info.0.json') as resp: #getting data
        data = await resp.json() #Pulling data
    num = data['num']
    alt = data['alt']
    title = data['safe_title']
    desc = f'{alt} Link to the original [here](https://xkcd.com/{num}).'
    em = discord.Embed(title=f'{title}: #{num}', color = 0x000000, description = desc) #Because black is nice.
    em.set_image(url = data['img']) #making embed
    em.set_footer(text=f'Requested by {ctx.message.author.display_name}')
    return em


token = os.getenv("DISCORD_TOKEN")
bot.run(token)  # Starts the bot