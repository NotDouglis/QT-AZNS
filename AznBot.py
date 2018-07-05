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
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    baseurl = ('https://idol.sankakucomplex.com/?tags=-animated+-video')
    endurl = ('&commit=Search')
    fullurl = (baseurl + '+' + msg + endurl)
    page = requests.get(fullurl, headers=headers)
    pagetext = page.text
    soup = BeautifulSoup(pagetext, "lxml")
    images = []
    num = 1
    for img in soup.find_all('img'):
        images.append(img.get('src'))
    imageurl = (random.choice(images))
    fixedimageurl = ("https:"+imageurl)
    print(fixedimageurl)
    embed = discord.Embed(title="QT Azn")
    embed.set_image(url=fixedimageurl)     
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
<<<<<<< HEAD
    embed.add_field(name="Meme Commands",value="mP-->Points the classical pointy finger at your target\nmSex-->Spells out the classical SEX meme")
    embed.add_field(name="Random/Test Commands",value="rCoin-->Flips a coin, heads or tails, buddy.\nrRng(MinNumber, MaxNumber)-->Generates a random number between the provided integers")
    embed.add_field(name="Webcrawling Commands",value="wWikipedia(ArticleName)-->Takes data from the given article\nwIdol(TagName)-->Returns a random image from Idol Complex with the given tag")
=======
    embed.add_field(name="Meme Commands",value="mP   --> Points the classical pointy finger at your target\nmSex --> Spells out the classical SEX meme")
    embed.add_field(name="Random/Test Commands",value="rCoin --> Flips a coin, heads or tails, buddy.\nrRng  --> Generates a random number between the provided integers\n     Parameters --> MinNumber: int\n                --> MaxNumber: int")
    embed.add_field(name="Webcrawling Commands",value="wWikipedia --> Takes data from the given article\n     Parameters --> ArticleName: str")
>>>>>>> 1b938e33775c6b2c976882824a6976446c81ae6e
    await bot.say(embed=embed)

#Code to connect py with bot
bot.run('NDYzOTI2NTU5OTE3NjA0ODY0.Dh3sng.0awcnUd5UQbQ201arZVkllA980c')
    

