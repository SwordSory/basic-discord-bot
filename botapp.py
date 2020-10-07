import discord
import random
import discord as disc
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import secrets
from time import sleep


client = commands.Bot(command_prefix=".")
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Making me better!!!"))
    print("Hello there! I am Evolution Wing bot at your service.")


@client.event
async def on_member_join(member):
    print(f"{member} has joined. Welcome! I hope you will have fun. :)")


@client.event
async def on_member_remove(member):
    print(f"{member} has left the server. Very sad :(")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing Argument.\nPlease Enter All Required Arguments.\n")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Command Not Found.\nType .help To See All The Existing Commands.\n")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Missing Permission.\nYou Cannot Use This Command.\n")


@client.command()
async def ping(ctx):
    await ctx.send(f"(:  Ping right now -> {round(client.latency * 1000)}ms <- Ping right now  :)")


@client.command()
async def serverhelp(ctx):
    await ctx.send("Ping someone with admin perms for help.")


@client.command(aliases=['gm',"morning"])
async def goodmorning(ctx):
    await ctx.send("Good morning! Have a nice day.")


@client.command(aliases=['gn',"night"])
async def goodnight(ctx):
    await ctx.send("Good night! Sleep well.")


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command(aliases=["flip",'coinflip',"Coin",'Coinflip',"Flip"])
async def coin(ctx):
    options = ["Head", "Tails", 'Lost the coin! cannot verify the results. Try again']
    result = random.choice(options)
    await ctx.send(result)


@client.command(aliases=["yo",'hay',"Yo",'Hay',"Hi"], pass_context=True)
async def hi(ctx, member : discord.Member):
    await ctx.send(f"Hay, {member.mention}  What are you doing? \nIs your day going nicely?\n")
    await client.delete_message(ctx.message)


@client.command(aliases=["Bye"])
async def bye(ctx):
    await ctx.send("sayonara")


@client.command(aliases=["Help",'HELP'])
async def help(ctx):
    await ctx.send("""Evolution Wing Official Discord Bot
    """)


client.run("NzYyOTU0NjU3OTM2ODM0NTYw.X3wq5Q.Br5mB_Qo8r1oX3lvJVRqmJLneQo")