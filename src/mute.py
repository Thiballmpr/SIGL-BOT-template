from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

@bot.command()
async def mute(ctx):
    await ctx.send('pong')