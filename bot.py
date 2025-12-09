import discord
from discord.ext import commands

#import economy functions
from economy import getBalance, addBalance, COINS_PER_MESSAGE

# import token
from config import TOKEN

#set intents
intents = discord.Intents.default()
intents.message_content = True  #this allows you to read message content

#bot settings
bot = commands.Bot(
    command_prefix="!", 
    intents = intents, 
    help_command=None
    )

#when bot is ready, it sends message in terminal
@bot.event
async def on_ready():
    print(f"bot is online!")

@bot.event
async def on_message(message: discord.message):

    """When users send a message, they recieve 1 coin."""

    #ignore bot messages
    if message.author.bot:
        return
    
    #ignore dms, should only work in server
    if message.guild is None:
        return
    
    #ignore messages that are commands
    if message.content.startswith("!"):
        await bot.process_commands(message)
        return
    
    addBalance(message.author.id, COINS_PER_MESSAGE)

    await bot.process_commands(message)

@bot.command(
    name="help",
    help="Gives command descriptions.",
    usage="!help"
)
async def help(ctx, commandName: str = None):
    
    """My custom help command."""
    if commandName is None:
        userLines = []
        adminLines = []
        allLines = []

        for command in bot.commands:
            line = (f"!{command.name} - {command.help}")

            admin = command.extras.get("admin", False)

            if admin:
                adminLines.append(line)
            else:
                userLines.append(line)

        allLines.append("**User Commands:**")
        allLines.extend(userLines)

        allLines.append("\n**Admin Commands:**")
        allLines.extend(adminLines)

        await ctx.send("\n".join(allLines))
        return

    command = bot.get_command(commandName)

    await ctx.send(f"**Command Name:** {command.name}\n**Description:** {command.help}\n**Usage:** {command.usage}")
    return


@bot.command(
    name="balance",
    help="Check your current coin balance.",
    usage="!balance",
    )
async def balance(ctx):

    """Sends user their current coin balance."""

    user = ctx.author
    amount = getBalance(user.id)

    word = "coin" if amount == 1 else "coins"

    await ctx.send(f"{user.mention} has {amount} {word}.")


@bot.command(
    name="give",
    help="Give coins to a user.",
    usage="!give @user amount",
    extras={"admin": True}
    )
@commands.has_permissions(manage_guild=True)
async def give(ctx, member: discord.Member, amount: int):

    """Give an amount of coins to a specific user. Admin only."""

    if amount <= 0:
        await ctx.send("invalid amount")
        return
    
    addBalance(member.id, amount)


bot.run(TOKEN)