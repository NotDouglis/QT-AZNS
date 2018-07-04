#Imports
import discord
import asyncio
from discord.ext import commands

#Initialize
client = discord.Client()#Creates Client
bot = commands.Bot(command_prefix='!')#Sets prefix for commands(!Command)

#Code
@bot.command()
async def SexCommand():
    await bot.say('S')
    asyncio.sleep(1)
    await bot.say('E')
    asyncio.sleep(1)
    await bot.say('X')
    asyncio.sleep(1)
    await bot.say('SEX')
    asyncio.sleep(1)

    
#Code to connect py with bot
bot.run('NDYzOTI2NTU5OTE3NjA0ODY0.Dh3sng.0awcnUd5UQbQ201arZVkllA980c')
    

