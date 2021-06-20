import discord
import os
from discord.ext import commands
import webrepl

TOKEN = os.environ["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix=['mr ', 'Mr ', 'mr', 'Mr'])
client = discord.Client()

repl=webrepl.Webrepl(**{'host':'192.168.0.105','port':8266,'password':'smith123'})

@bot.command(name="turn")
async def nodemcu(ctx, status="on"):
    resp = repl.sendcmd("lights=machine.Pin(16, machine.Pin.OUT);")
    resp = repl.sendcmd("fan=machine.Pin(2, machine.Pin.OUT);")
    if status == "on":
        resp = repl.sendcmd("lights.value(0)")
        resp = repl.sendcmd("fan.value(1)")
        await ctx.send(f"{ctx.author} toggled the device.")
    else:
        resp = repl.sendcmd("lights.value(1)")
        resp = repl.sendcmd("fan.value(0)")
        await ctx.send(f"{ctx.author} toggled the device.")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has hacked into Discord :)\n')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name='Mr Robot'))

@bot.command(name='ping')
async def _ping_(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    message = discord.Embed(
        title=f"My ping is {ping}ms")
    await ctx.send(embed=message)


bot.run(TOKEN)
