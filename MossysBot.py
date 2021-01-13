# bot.py
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

load_dotenv()

intents = discord.Intents.default()
intents.members = True

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

random.seed(random.random())

bot = commands.Bot(command_prefix="/", intents=intents)

def find_member(strmember):
    for member in guild.members:
        if str(member) == strmember:
            return member

def parse_images(string):
    imgs = []
    tmpimg = ""
    for c in string:
        if c != " ":
            tmpimg += c
        else:
            imgs.append(tmpimg)
            tmpimg = ""
    imgs.append(tmpimg)
    return imgs

@bot.event
async def on_ready():
    global guild 
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print("Connected to " + str(guild.name))
    print("Current members:")
    for member in guild.members:
        print(member)

@bot.command(name="rand", help="picks a random person's name or pfp and displays it. syntax: /rand [name, pfp] [name, pfp] ...")
async def idiot(ctx, *infos):
    randmember = guild.members[random.randrange(0, len(guild.members))]
    for info in infos:
        if info.lower() == "name":
            await ctx.send(randmember.name)
        elif info.lower() == "pfp":
            await ctx.send(randmember.avatar_url)

@bot.command(name="echo", help="repeat a message. syntax: /echo message")
async def echo(ctx, *messages):
    completemessage = ""
    for message in messages:
        completemessage += message + " "
    if completemessage.lower() == "i am stupid ":
        await ctx.send("no, you are")
    else:
        await ctx.send(completemessage)

@bot.command(name="dm", help="direct message someone something. syntax: /dm message")
async def dm(ctx, strrecipient, *messages):
    completemessage = ""
    for message in messages:
        completemessage += message + " "
    recipient = find_member(strrecipient)
    if recipient:
        channel = await recipient.create_dm()
        await channel.send(completemessage)

@bot.command(name="reddit", help="get the hottest images from a subreddit. syntax: /rand subreddit number_of_images(default 3) ...")
async def reddit(ctx, subreddit, *num):
    imgnum = 3
    if len(num) > 0:
        if int(num[0]) <= 10:
            imgnum = num[0]
    os.system("./mossysbotgetred " + subreddit + " " + str(imgnum))
    try:
        redimgs = open("redimgs", "r")
        imgs = parse_images(redimgs.read())
        for img in imgs:
            await ctx.send(img)
    except IOError:
        await ctx.send("Subbreddit does not exist")
    redimgs.close()

bot.run(TOKEN)