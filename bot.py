import discord
from discord.ext import commands

# import token
from config import TOKEN

#set intents
intents = discord.Intents.default()
intents.message_content = True  #this allows you to read message content

#set prefix for commands
bot = commands.Bot(command_prefix="!", intents = intents)

#when bot is ready, it says text
@bot.event
async def on_ready():
    print(f"bot is online!")

@bot.command()
async def test(ctx):
    await ctx.send("hi")

bot.run(TOKEN)