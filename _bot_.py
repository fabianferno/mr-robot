import discord
import random
import asyncio
import youtube_dl
import json
import shutil
import os
from datetime import datetime
from discord.ext import commands
from discord.utils import get

# from discord.voice_client import VoiceClient

TOKEN = 'NzI3MDU5OTg0OTg2NDA2OTEy.XvpKQg.nV32LI46fkX3e7PV3x_NtfTHkew'
bot = commands.Bot(command_prefix=['mr ', 'Mr '])


@bot.event
async def on_ready():
    print(f'{bot.user.name} has hacked into Discord :)')
    # channel = bot.get_channel(699097908846526474)
    # await channel.send(f'{bot.user.name} has hacked into Discord :)')


com = ["jessi", "class", "feeling", "sayhello", "said", "gd", "johnny", "rascal", "msg", "coffee",
       "sangeetha", "thala", "amuk", "yeo", "money", "pokiri", "happy", "oho", "paavam", "raama", "canada",
       "yblood", "steve", "bestfrnd"]

ran = random.choice(com)

#testing the version control system


@bot.command(name="name")
async def _name(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('mr.robot.wav'), after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="leave")
async def leave(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
        print(f"\n{bot.user.name} was disconnected from {channel} by {ctx.author} ")
    else:
        await ctx.send(f"I'm not connected to any voice channel")
        print(f"\nAuthor is not connected to any voice channel")


@bot.command(name="suicide")
async def leave(ctx):
    await ctx.send(f"hahaha")
    print(f"\n{ctx.author} shut me down")
    exit()


@bot.command(name='kanmani', pass_context=True)
async def kanmani(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('Kanmani-Anbodu.mp3'), after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name='jessi', pass_context=True)
async def jessi(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('jessi.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='yeo', pass_context=True)
async def jessi(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('raja_rani.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='class', pass_context=True)
async def cl(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('vasulraja_class.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='feeling', pass_context=True)
async def feel(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    await vc.play(discord.FFmpegPCMAudio('each_girl_each_feel.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='sayhello', pass_context=True)
async def hfrnd(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('Say_Hello_To_My_Little_Friend.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='said', pass_context=True)
async def said(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('said.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='gd', pass_context=True)
async def gd(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('im_gd.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='johnny', pass_context=True)
async def shine(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('here_jonny.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='rascal', pass_context=True)
async def rascal(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('rascal.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='alone', pass_context=True)
async def alone(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('alone.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='msg', pass_context=True)
async def msg(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('message.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='fam', pass_context=True)
async def fam(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('laaa_la_la_laa.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='oho', pass_context=True)
async def oho(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('diluwale.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='happy', pass_context=True)
async def happy(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('be_happy.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='canada', pass_context=True)
async def canada(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('canadala_periya_drums_player.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='yblood', pass_context=True)
async def yblood(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('why_blood_same_blood.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='money', pass_context=True)
async def money(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('money_comes_today_goes_tomorrow.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='steve', pass_context=True)
async def steve(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('i_am_steve_wak.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='bestfrnd', pass_context=True)
async def best_frnd(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('i_am_your_best_frnd.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='raama', pass_context=True)
async def raama(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('aiyo_rama.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='paavam', pass_context=True)
async def pavam(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('ungala_paatha_paavama_iruku.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='coffee', pass_context=True)
async def sukku(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('sukku_coffee.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='sangeetha', pass_context=True)
async def sng(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('sangeetha.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='amuk', pass_context=True)
async def dumuk(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('amal_dumal.mp3'), after=lambda e: print('Done\n', '_' * 10))
    vc.is_playing()


@bot.command(name='thala', pass_context=True)
async def thala(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('ena_thala.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='pokiri', pass_context=True)
async def pok(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('pokkiri.mp3'), after=lambda e: print('Done\n', '_' * 10))


@bot.command(name="s")
async def don():
    # music_channel = bot.get_channel(698175839283707914)
    # ty_comm = bot.get_channel(698202399537496166)
    code_here = bot.get_channel(699097908846526474)
    # await music_channel.send(f'Indeed')
    # await ty_comm.send(f'bye')
    await code_here.send(f'')


@bot.command(name="call")
async def bring(ctx):
    # jesin = bot.get_user(706039145642065971)
    # josh = bot.get_user(698368879478702091)
    # fab = bot.get_user(299152387728343043)
    # jon = bot.get_user(485814814095179777)
    abi = bot.get_user(698479658198499389)
    # await jesin.send(f'{ctx.author} is calling you')
    await abi.send(f'{ctx.author} is calling you')
    # await josh.send(f'{ctx.author} is calling you')
    # await fab.send(f'{ctx.author} is calling you')
    # await jon.send(f'{ctx.author} is calling you')
    print("Done\n")


@bot.command
async def dont(ctx):
    user = bot.get_user(698368879478702091)
    print(user)
    if ctx.author == user:
        await ctx.send(f"You are not allowed")


@bot.command(name='ping')
async def _ping_(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.send(f"My ping is {ping}ms")


@bot.command(name='love')
async def abirami(ctx):
    response = "மனிதர் உணர்ந்து கொள்ள இது மனிதக் காதலல்ல!"
    await ctx.send(response)


@bot.command(name='hi')
async def welcometxt(ctx):
    response = "Welcome to Ferno's Server"
    await ctx.send(response)


@bot.command(name='fsociety')
async def abirami(ctx):
    response = "Save the World form Humans"
    await ctx.channel.send(file=discord.File('mrrobot.png'))
    await ctx.send(response)


@bot.command(name='likes')
async def liking(ctx, obj1, obj2):
    response = f"Fabian likes {obj1} and {obj2}. Do you like {obj1} and {obj2}?"
    await ctx.send(response)


@bot.command(name='hello')
async def skywalker(ctx):
    if ctx.author == "jesinthan#0280":
        await ctx.send(f"{ctx.author} is not allowed to talk here!!")


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to Fabian\'s server!'
    )


# Find Date of Birth
@bot.command(name='dob')
async def date_of_birth(ctx, birth_d: int, birth_m: int, birth_y: int):
    try:
        now = datetime.now()
        year = now.year
        month = now.month
        date = now.day
        y_child = year - birth_y
        m_child = month - birth_m
        d_child = date - birth_d

        if birth_y <= 0:
            await ctx.send("\nEnter a valid Birth Year")
        elif birth_m <= 0 or birth_m >= 13:
            await ctx.send("\nEnter a valid Birth Month")
        elif birth_d <= 0 or birth_d >= 32:
            await ctx.send("\nEnter a valid Birth Date")
        elif y_child < 0 or (y_child == 0 and m_child < 0) or (
                y_child == 0 and m_child == 0 and d_child < 0):
            await ctx.send("Dude! you are not born yet")
        elif y_child == 0:
            if m_child == 0:
                await ctx.send(f"Your are {d_child} day(s) old")
            else:
                await ctx.send(
                    f"Your are {m_child} month(s) and {d_child} day(s) old"
                )
        elif month > birth_m:
            await ctx.send(f"Your age is {y_child}")
        elif month == birth_m:
            if date > birth_d or date == birth_d:
                await ctx.send(f"Your age is {y_child}")
            else:
                fin = y_child - 1
                await ctx.send(f"Your age is {fin}")
        else:
            fin = y_child - 1
            await ctx.send(f"Your age is {fin}")

    except ValueError:
        await ctx.send(f"Enter: Date, Month, Year")


bot.run(TOKEN)
