import discord
import random
<<<<<<< HEAD:robot.py
import asyncio
#import youtube_dl
import json
import shutil
=======
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py
import os
import io
import wikipedia
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
from discord import File
from datetime import datetime
from discord.ext import commands
from discord.utils import get


<<<<<<< HEAD:robot.py
TOKEN = 'NzI3MDU5OTg0OTg2NDA2OTEy.XvmVYA.5w6cPraEGQqKks9_TqqLFlIAOHw'
bot = commands.Bot(command_prefix=['mr ', 'Mr '])
=======
TOKEN = os.environ["DISCORD_TOKEN"]
bot = commands.Bot(command_prefix=['mr ', 'Mr ', 'mr', 'Mr'])
client = discord.Client()


'''@bot.event
async def on_member_join(member):
    image_width = 1920
    image_height = 940

    image = Image.open('welcome1.jpg')

    draw = ImageDraw.Draw(image)

    channel = get(member.guild.channels, name="how-i-met-everyone")

    text = f'{member}'
    text = str(text)
    text = text[:-5]
    total_small = f'{member.guild.member_count}'
    welcome_msg = f'welcome to the office'

    if len(text) > 19:
        font = ImageFont.truetype('hack_font.ttf', 80)
    else:
        font = ImageFont.truetype(r'hack_font.ttf', 100)

        small_font = ImageFont.truetype(r'hack_font.ttf', 70)

        big_font = ImageFont.truetype(r'hack_font.ttf', 120)

    text_width, text_height = draw.textsize(text, font=font)
    x = (image_width - text_width) // 2 + 0
    y = (image_height - text_height) // 2 + 410
    draw.text((x, y), text, fill=(255, 255, 255), font=font)

    text_width, text_height = draw.textsize(total_small, font=font)
    x = (image_width - text_width) // 2 - 890
    y = (image_height - text_height) // 2 + 440
    draw.text((x, y), total_small, fill=(255, 255, 255), font=small_font)

    text_width, text_height = draw.textsize(total_small, font=font)
    x = (image_width - text_width) // 2 - 500
    y = (image_height - text_height) // 2 + 300
    draw.text((x, y), welcome_msg, fill=(255, 255, 255), font=big_font)

    avatar_size = 128
    rect_x0 = 835
    rect_y0 = 90

    avatar_asset = member.avatar_url_as(format='jpg', size=avatar_size)

    buffer_avatar = io.BytesIO(await avatar_asset.read())

    avatar_image = Image.open(buffer_avatar)

    avatar_image = avatar_image.resize((250, 250))

    circle_image = Image.new('L', (250, 250))
    circle_draw = ImageDraw.Draw(circle_image)
    circle_draw.ellipse((0, 0, 250, 250), fill=255)

    image.paste(avatar_image, (rect_x0, rect_y0), circle_image)

    buffer = io.BytesIO()

    image.save(buffer, format='PNG')

    buffer.seek(0)
    await channel.send(file=File(buffer, 'myimage.png'))
    print(f"{member} has entered into the server")
'''


@bot.command("welcome")
async def welcome_(ctx):
    image_width = 1920
    image_height = 940

    image = Image.open('welcome1.jpg')

    draw = ImageDraw.Draw(image)

    # channel = get(ctx.guild.channels)
    # channel2 = str(channel)

    text = f'{ctx.author}'
    text = str(text)
    text = text[:-5]
    total_small = f'{ctx.author.guild.member_count}'
    welcome_msg = f'welcome to the office'

    if len(text) > 19:
        font = ImageFont.truetype('hack_font.ttf', 80)
    else:
        font = ImageFont.truetype(r'hack_font.ttf', 100)

        small_font = ImageFont.truetype(r'hack_font.ttf', 70)

        big_font = ImageFont.truetype(r'hack_font.ttf', 120)

    text_width, text_height = draw.textsize(text, font=font)
    x = (image_width - text_width) // 2 + 0
    y = (image_height - text_height) // 2 + 410
    draw.text((x, y), text, fill=(255, 255, 255), font=font)

    text_width, text_height = draw.textsize(total_small, font=font)
    x = (image_width - text_width) // 2 - 890
    y = (image_height - text_height) // 2 + 440
    draw.text((x, y), total_small, fill=(255, 255, 255), font=small_font)

    text_width, text_height = draw.textsize(total_small, font=font)
    x = (image_width - text_width) // 2 - 500
    y = (image_height - text_height) // 2 + 300
    draw.text((x, y), welcome_msg, fill=(255, 255, 255), font=big_font)

    avatar_size = 128
    rect_x0 = 835
    rect_y0 = 90

    avatar_asset = ctx.author.avatar_url_as(format='jpg', size=avatar_size)

    buffer_avatar = io.BytesIO(await avatar_asset.read())

    avatar_image = Image.open(buffer_avatar)

    avatar_image = avatar_image.resize((250, 250))

    circle_image = Image.new('L', (250, 250))
    circle_draw = ImageDraw.Draw(circle_image)
    circle_draw.ellipse((0, 0, 250, 250), fill=255)

    image.paste(avatar_image, (rect_x0, rect_y0), circle_image)

    buffer = io.BytesIO()

    image.save(buffer, format='PNG')

    buffer.seek(0)
    await ctx.send(file=File(buffer, 'myimage.png'))
    print(f"{ctx.author} entered welcome")
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.event
async def on_ready():
    print(f'{bot.user.name} has hacked into Discord :)\n')
    channel = bot.get_channel(760774435950821386)
    await channel.send(f'{bot.user.name} has hacked into Discord :)')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name='Mr Robot'))


com = ["jessi", "class", "feeling", "sayhello", "said", "gd", "johnny", "rascal", "msg", "coffee",
<<<<<<< HEAD:robot.py
       "sangeetha", "thala", "amuk", "yeo", "money", "pokiri", "happy", "oho", "paavam", "raama", "canada",
       "yblood", "steve", "bestfrnd"]

ran = random.choice(com)
=======
       "sangeetha", "thala", "amuku", "yeo", "money", "pokiri", "happy", "oho", "fam", "pavam", "rama",
       "canada", "yblood", "steve", "bestfrnd", "thirumba", "ponnu", "ready", "tension", "nonsense", "riddle",
       "identity", "ahaan", "vambu", "varutham", "shobba", "usupethi", "unakenapa", "ignore100", "plan", "stay",
       "perumai"]


"""@bot.event
async def on_message(message):
    if message.content == "hello world":
        channel = bot.get_channel(699097908846526474)
        await channel.send(f'Did someone call me?')
        await bot.process_commands(message)
"""

>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py

@bot.command(name="leave")
async def leave(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
        print(f"\n{bot.user.name} was disconnected from {channel} by {ctx.author} ")
    else:
        await ctx.send(f"I'm not connected to any voice channel")
        print(f"Author is not connected to any voice channel\n")


@bot.command(name="suicide")
async def suicide(ctx):
    await ctx.send(f"hahaha")
    print(f"{ctx.author} shut me down\n")
    exit()

@bot.command(name="name")
async def _name(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('audio/mr.robot.wav'), after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="wiki")
async def wiki(ctx, *w):
    try:
        page = wikipedia.summary(str(w))
        page = page[0:2000]
        await ctx.send(f" {page}")
        print(f"{ctx.author} did wiki search on {w}")
    except:
        await ctx.send("Unable to search")
        print(f"{str(w)}Unable to search")


@bot.command(name="about")
async def embed(ctx):
    com2 = " | ".join(com)
    message = discord.Embed(
        title="In charge of humour, I am",
        description="Make sure you are connected to a voice channel before using the commands",
        color=ctx.author.color,
        # timestamp=ctx.message.created_at
    )
    message.set_author(
        name="Guidance",
        icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/320/whatsapp/238/robot-face_1f916.png"
    )
    message.add_field(name="Prefix each command with  Mr/mr", value=str(com2))
    message.add_field(name="A Karuthu for you",
                      value="Get a random voice\nType: Mr/mr luck", inline=False)
    message.add_field(name="For TTS", value='Use: Mrt/mrt', inline=False)
    message.add_field(name="To know briefly about something",
                      value='Use: Mr wiki/mr wiki and type the thing you wanna know', inline=False)
    message.add_field(name="To disconnect me",
                      value='Use: Mr/mr leave', inline=False)
    message.add_field(name="They created me, yes God exists".upper(),
                      value="<@299152387728343043> and <@698368879478702091>")
    # message.set_footer(text="")
    await ctx.send(embed=message)
    print(f"{ctx.author} displayed About\n")


@bot.command(name="t")
async def tts(ctx, *words):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    word = " ".join(words).lower()
    if voice:
        await voice.disconnect()
    await channel.connect()
    await ctx.send(f"{word}", tts=True)
    print(f"{ctx.author} said: {word}")


@bot.command(name="say")
async def name2(ctx, *words):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    word = " ".join(words).lower()

    # file = "welcome.mp3"
    # location = r"C:\Users\Joshua\PycharmProjects\First\discord_bot_"
    # path = os.path.join(location, file)
    # if file in location:
    #    os.remove(path)
    #    print("File removed")

    print("\nProcessing...")
    the_text = gTTS(text=word, lang='en', slow=True)
    the_text.save("welcome.mp3")
    print("File converted")
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('welcome.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="luck", pass_context=True)
async def random_(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    path = r"C:\Users\Joshua\PycharmProjects\First\discord_bot_\voices"
    voices = os.listdir(path)
    ran = random.choice(voices)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(ran),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="vambu")
async def vambu(ctx):
    try:
        channel = ctx.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice:
            await voice.disconnect()
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('vambu.mp3'),
                after=lambda e: print(f'Done\n', '_' * 10))
    except AttributeError:
        await ctx.send("Connect yourself to a voice channel")


@bot.command(name="varutham")
async def varutham(ctx):
    try:
        channel = ctx.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice:
            await voice.disconnect()
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('varutham.mp3'),
                after=lambda e: print(f'Done\n', '_' * 10))
    except AttributeError:
        await ctx.send("Connect yourself to a voice channel")


@bot.command(name="perumai")
async def perumai(ctx):
    try:
        channel = ctx.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice:
            await voice.disconnect()
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('perumai.mp3'),
                after=lambda e: print(f'Done\n', '_' * 10))
    except AttributeError:
        await ctx.send("Connect yourself to a voice channel")


@bot.command(name="stay")
async def stay(ctx):
    try:
        channel = ctx.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice:
            await voice.disconnect()
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('stay.mp3'),
                after=lambda e: print(f'Done\n', '_' * 10))
    except AttributeError:
        await ctx.send("Connect yourself to a voice channel")


@bot.command(name="plan")
async def plan(ctx):
    try:
        channel = ctx.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice:
            await voice.disconnect()
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('plan.mp3'),
                after=lambda e: print(f'Done\n', '_' * 10))
    except AttributeError:
        await ctx.send("Connect yourself to a voice channel")


@bot.command(name="theone")
async def the_one(ctx):
    try:
        channel = ctx.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice:
            await voice.disconnect()
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('theone.mp3'),
                after=lambda e: print(f'Done\n', '_' * 10))
    except AttributeError:
        await ctx.send("Connect yourself to a voice channel")


@bot.command(name="ignore100")
async def ignore100(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('ignore100.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="willing")
async def willing(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('willing.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="unakenapa")
async def unakenapa(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('unakenapa.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="identity")
async def identity(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('identity_theft.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="usupethi")
async def usupethi(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('usupethi.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="riddle")
async def riddle(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('riddle.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="ahaan")
async def ahaan(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('ahaan.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="nonsense")
async def nonsense(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('nonsense.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name="name")
async def _name(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('mr.robot.wav'),
            after=lambda e: print(f'Done\n', '_' * 10))


@bot.command(name='kanmani', pass_context=True)
async def kanmani(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/Kanmani-Anbodu.mp3'), after=lambda e: print(f'Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('Kanmani-Anbodu.mp3'),
            after=lambda e: print(f'Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='jessi', pass_context=True)
async def jessi(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/jessi.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    await vc.play(discord.FFmpegPCMAudio('jessi.mp3'), after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='yeo', pass_context=True)
async def yeo(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('raja_rani.mp3'),
            after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='tension', pass_context=True)
async def tension(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('less_tension_more_work.mp3'),
            after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='shobba', pass_context=True)
async def shobba(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('shobba.mp3'),
            after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='thirumba', pass_context=True)
async def thirumba(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('thirumba.mp3'),
            after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='ponnu', pass_context=True)
async def ponnu(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('ponnu.mp3'),
            after=lambda e: print('Done\n', '_' * 10))


@bot.command(name='ready', pass_context=True)
async def ready(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/raja_rani.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('ready.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='class', pass_context=True)
async def cl(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/vasulraja_class.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('vasulraja_class.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='feeling', pass_context=True)
async def feel(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    await vc.play(discord.FFmpegPCMAudio('audio/each_girl_each_feel.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('each_girl_each_feel.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='sayhello', pass_context=True)
async def hfrnd(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/Say_Hello_To_My_Little_Friend.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('Say_Hello_To_My_Little_Friend.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='said', pass_context=True)
async def said(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/said.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('said.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='gd', pass_context=True)
async def gd(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/im_gd.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('im_gd.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='johnny', pass_context=True)
async def shine(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/here_jonny.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('here_jonny.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='rascal', pass_context=True)
async def rascal(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/rascal.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('rascal.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='alone', pass_context=True)
async def alone(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/alone.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('alone.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='msg', pass_context=True)
async def msg(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/message.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('message.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='fam', pass_context=True)
async def fam(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/laaa_la_la_laa.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('laaa_la_la_laa.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='oho', pass_context=True)
async def oho(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/diluwale.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('diluwale.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='happy', pass_context=True)
async def happy(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/be_happy.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('be_happy.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='canada', pass_context=True)
async def canada(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/canadala_periya_drums_player.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('canadala_periya_drums_player.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='yblood', pass_context=True)
async def yblood(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/why_blood_same_blood.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('why_blood_same_blood.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='money', pass_context=True)
async def money(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/money_comes_today_goes_tomorrow.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('money_comes_today_goes_tomorrow.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='steve', pass_context=True)
async def steve(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/i_am_steve_wak.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('i_am_steve_wak.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='bestfrnd', pass_context=True)
async def best_frnd(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/i_am_your_best_frnd.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('i_am_your_best_frnd.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='rama', pass_context=True)
async def raama(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/aiyo_rama.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('aiyo_rama.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='pavam', pass_context=True)
async def pavam(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/ungala_paatha_paavama_iruku.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('ungala_paatha_paavama_iruku.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='coffee', pass_context=True)
async def sukku(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/sukku_coffee.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('sukku_coffee.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='sangeetha', pass_context=True)
async def sng(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/sangeetha.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('sangeetha.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='amuku', pass_context=True)
async def dumuk(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/amal_dumal.mp3'), after=lambda e: print('Done\n', '_' * 10))
    vc.is_playing()
=======
    vc.play(discord.FFmpegPCMAudio('amal_dumal.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='thala', pass_context=True)
async def thala(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/ena_thala.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('ena_thala.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name='pokiri', pass_context=True)
async def pok(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice:
        await voice.disconnect()
    vc = await channel.connect()
<<<<<<< HEAD:robot.py
    vc.play(discord.FFmpegPCMAudio('audio/pokkiri.mp3'), after=lambda e: print('Done\n', '_' * 10))
=======
    vc.play(discord.FFmpegPCMAudio('pokkiri.mp3'),
            after=lambda e: print('Done\n', '_' * 10))
>>>>>>> 5ea5d9ab1fa92b23990d0c9dd95922a423266bef:_bot_.py


@bot.command(name="s")
async def don():
    # music_channel = bot.get_channel(698175839283707914)
    # ty_comm = bot.get_channel(698202399537496166)
    init = bot.get_channel(744872563553075270)
    # code_here = bot.get_channel(699097908846526474)
    # await code_here.send(f'')
    await init.send(f'Hello Jonathan')


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


@bot.command(name='ping')
async def _ping_(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    message = discord.Embed(
        title=f"My ping is {ping}ms")
    await ctx.send(embed=message)


@bot.command(name='love')
async def abirami(ctx):
    response = "மனிதர் உணர்ந்து கொள்ள இது மனிதக் காதலல்ல!"
    await ctx.send(response)


@bot.command(name='hi')
async def welcometxt(ctx):
    response = "Welcome to Ferno's Server"
    await ctx.send(response)


@bot.command(name='fsociety')
async def fsociety(ctx):
    response = "Save the World form Humans"
    await ctx.channel.send(file=discord.File('img.jpg'))
    await ctx.send(response)


@bot.command(name='likes')
async def liking(ctx, obj1, obj2):
    response = f"Fabian likes {obj1} and {obj2}. Do you like {obj1} and {obj2}?"
    await ctx.send(response)


@bot.command(name='hello')
async def skywalker(ctx):
    if ctx.author == "jesinthan#0280":
        await ctx.send(f"{ctx.author} is not allowed to talk here!!")


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
