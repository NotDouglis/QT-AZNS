#Imports
import discord
import asyncio
import random
import requests
import urllib
from bs4 import BeautifulSoup
from discord.ext import commands
from urllib.request import urlopen


#Initialize
client = discord.Client()#Creates Client
bot = commands.Bot(command_prefix='!')#Sets prefix for commands(!Command)

#Code
#Resource Crawling
@bot.command()
async def wWikipedia(msg):
    pagetoget = ('http://simple.wikipedia.org/wiki/'+msg)
    page = requests.get(pagetoget)
    soup = BeautifulSoup(page.content, "lxml")
    allTexts = soup.find_all('b')
    for i in range(0, 8):
        printstr = (i+1, " : ", allTexts[i])
        await bot.say(printstr)

@bot.command()
async def wIdol(msg):
    baseurl = ('https://idol.sankakucomplex.com/?tags=-animated+-video')
    endurl = ('&commit=Search')
    fullurl = (baseurl + '+' + msg + endurl)
    soup = BeautifulSoup(urlopen(fullurl).read())
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    imageurl = (random.choice(images))
    embed = discord.Embed(title="QT Azn")
    embed.set_image(url=imageurl)
    await bot.say(embed=embed)
    
#Memes
@bot.command()
async def mP():
    await bot.say(':point_right:')

@bot.command()
async def mSex():
    await bot.say('S')
    asyncio.sleep(1)
    await bot.say('E')
    asyncio.sleep(1)
    await bot.say('X')
    asyncio.sleep(1)
    await bot.say('SEX')
    asyncio.sleep(1)

#Random Stuff
@bot.command()
async def rCoin():
    Result = ""
    RandomNumber = random.randint(0,1)
    if(RandomNumber == 0):
        Result = "Heads"
    elif(RandomNumber == 1):
        Result = "Tails"
    await bot.say(Result)
    

@bot.command()
async def rRNG(MinNumber: int , MaxNumber: int):
    RandomNumber = random.randint(MinNumber,MaxNumber)
    await bot.say(str(RandomNumber))

#Help
@bot.command()
async def Help():
    #Title
    embed = discord.Embed(title="Help")
    #Help
    embed.add_field(name="Meme Commands",value="mP-->Points the classical pointy finger at your target\nmSex-->Spells out the classical SEX meme")
    embed.add_field(name="Random/Test Commands",value="rCoin-->Flips a coin, heads or tails, buddy.\nrRng(MinNumber, MaxNumber)-->Generates a random number between the provided integers")
    embed.add_field(name="Webcrawling Commands",value="wWikipedia(ArticleName)-->Takes data from the given article")
    await bot.say(embed=embed)

#Code to connect py with bot
bot.run('NDYzOTI2NTU5OTE3NjA0ODY0.Dh3sng.0awcnUd5UQbQ201arZVkllA980c')
    

