#Imports
import discord
import asyncio
import random
import requests
import urllib
import json
from bs4 import BeautifulSoup
from discord.ext import commands
from urllib.request import urlopen


#Initialize
client = discord.Client()#Creates Client
bot = commands.Bot(command_prefix='!')#Sets prefix for commands(!Command)

#Code
#Resource Crawling
#Wikipedia
@bot.command()
async def wWikipedia(msg):
    pagetoget = ('http://simple.wikipedia.org/wiki/'+msg)
    page = requests.get(pagetoget)
    soup = BeautifulSoup(page.content, "lxml")
    allTexts = soup.find_all('b')
    for i in range(0, 8):
        printstr = (i+1, " : ", allTexts[i])
        await bot.say(printstr)

#Crystal Math Labs
@bot.command()
async def wCML(Username: str,Skill: str,Time: str):
    #Get User Page
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    initialurl = "https://crystalmathlabs.com/tracker/track.php?player="
    playerurl = (initialurl + Username)
    TimeStr = "1 Week"
    if(Time.lower() == 'd'):
        playerurl += "&time=1d"
        TimeStr = "1 Day"
        
    elif(Time.lower() == 'w'):
        pass
    
    elif(Time.lower() == 'm'):
        playerurl += "&time=31d"
        TimeStr = "1 Month"

    elif(Time.lower() == 'y'):
        playerurl += "&time=365d"
        TimeStr = "1 Year"

    elif(Time.lower() == 'a'):
        playerurl += "&time=all"
        TimeStr = "All Time"
        
    page = requests.get(playerurl, headers=headers)
    pagetext = page.text
    soup = BeautifulSoup(pagetext, "lxml")
    content = soup.find(id="content")
    strcontent = (str(content))
    SkillFound = 0

    #Check If User Exists - Done
    if ("No data" in strcontent):
        embed = discord.Embed(title="Error")
        embed.add_field(name="You messed up!", value="User doesn't exist")    
        await bot.say(embed=embed)
    else:
        #Get Skill Data - Done
        for tr in soup.findAll("tr"):
            content = soup.findAll("tr")
            #Get Row where skill is
            if(tr.find('a').text.lower() == Skill.lower()):
                #Get Individual Table Data
                tdarray = []
                for td in tr:
                    tdarray.append(td)                 
                SkillName = tdarray[0].find('img').get('title')
                SkillImage = "https://crystalmathlabs.com/tracker/" + tdarray[0].find('img').get('src')
                XPGained = tdarray[1].text
                SkillFound = 1
                embed = discord.Embed(title=""+Username+": "+SkillName+" - " + TimeStr)
                embed.set_image(url=SkillImage)
                embed.add_field(name="XP Gained",value=XPGained)    
                await bot.say(embed=embed)
                break
                
        if(SkillFound == 0):
            embed = discord.Embed(title="Error2")
            embed.add_field(name="You messed up!", value="Skill doesn't exist")    
            await bot.say(embed=embed)

        
    
@bot.command()
async def wIdol(msg):
    await bot.say("Granting Request, please wait...")
    #Logging In
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    #Getting Url With Tags
    baseurl = ('https://idol.sankakucomplex.com/?tags=-animated+-video')
    endurl = ('&commit=Search')
    fullurl = (baseurl + '+' + msg + endurl)
    #Requesting Data for Pages
    page = requests.get(fullurl, headers=headers)
    pagetext = page.text
    soup = BeautifulSoup(pagetext, "lxml")
    pagelinks = []
    count = 1
    leaveloop = 0
    page2 = 0
    
    #Getting all possible pages: Page2 = endswith(page=2)|Page3+ = startswith(/?next)
    pagelinks.append("?tags=-animated+-video" + "+" + msg + "&page=1")
    print(pagelinks[0])
    while(leaveloop != 1):
        nolinks = 0
        page = requests.get(fullurl, headers=headers)
        pagetext = page.text
        soup = BeautifulSoup(pagetext, "lxml")
        for link in soup.find_all('a'):
            if(link.get('href')):
                if(link.get('href').startswith("/?next")):
                    print("Next If")
                    print(count)
                    print(link.get('href'))
                    fullurl = ('https://idol.sankakucomplex.com' + link.get('href'))
                    count += 1
                    pagelinks.append(link.get('href'))
                    nolinks = 1
                    
                elif(link.get('href').endswith("page=2")):
                    if(page2 == 0):
                        print("Page2 If")
                        print(count)
                        print(link.get('href'))
                        fullurl = ('https://idol.sankakucomplex.com' + link.get('href'))
                        count += 1  
                        pagelinks.append(link.get('href'))
                        nolinks = 1
                        page2 = 1
                else:
                    pass
                
        if(nolinks == 0):
            leaveloop = 1
            pass
    
    #Requesting Data for Images
    pageurl = (random.choice(pagelinks))
    print('-')
    print(pageurl)
    imageurl = ("https://idol.sankakucomplex.com" + pageurl)
    page = requests.get(imageurl, headers=headers)
    pagetext = page.text
    soup = BeautifulSoup(pagetext, "lxml")
    links = []
    count = 1
    #Adding Image URLs
    for link in soup.find_all('a'):
        if(link.get('href')):
            if(link.get('href').startswith("/post/show")):
                print(count)
                print(link.get('href'))
                count += 1
                links.append(link.get('href'))
            else:
               pass
        else:
            pass
    #RNG
    linkurl = (random.choice(links))
    posturl = ("https://idol.sankakucomplex.com" + linkurl)
    #Getting Post Image
    page = requests.get(posturl, headers=headers)
    pagetext = page.text
    soup = BeautifulSoup(pagetext, "lxml")
    images = []
    for img in soup.find_all('img'):
        if(img.get('src').startswith("https://")):
            pass
        elif(img.get('src').endswith("logo.png")):
            pass
        else:
            print('-----------------')
            print(img.get('src'))
            if((img.get('src')).startswith("//is.sankakucomplex.com/")):
                if((img.get('src')).startswith("//is.sankakucomplex.com/data/preview")):
                    pass
                else:
                    images.append(img.get('src'))
    #Print
    fixedimageurl = ("https:"+images[0])
    print(fixedimageurl)
    embed = discord.Embed(title="QT Azn")
    embed.set_image(url=fixedimageurl)
    embed.add_field(name="Source",value=fixedimageurl)    
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
    embed.add_field(name="Webcrawling Commands",value="wWikipedia(ArticleName)-->Takes data from the given article\nwIdol(TagName)-->Returns a random image from Idol Complex with the given tag")
    await bot.say(embed=embed)

#Code to connect py with bot
bot.run('NDY2NjMxNjgxNzk4MDQ1NzE2.Die4Og.PuqIvvcCTwK4X6YWY8zO-bd9v3c')
