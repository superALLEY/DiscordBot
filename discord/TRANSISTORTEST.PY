import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
import os
import asyncio

client = commands.Bot(command_prefix="=",intents=discord.Intents.all())

bot_status = cycle(["https://discord.gg/eQ97mKH4","join our server","TO game && TO study!!","stop looking at me","sype in '=help' for help"])   
@tasks.loop(seconds=5)  
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status))) 

@client.event
async def on_ready():
    print("succes: Bot is connected to Discord")
    change_status.start()

async def load():
    for filename in os.listdir(".\\cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
            await print(f"{filename[:-3]} is loaded")

async def main():
    async with client:
        await load()
        await client.start()


#ping
@client.command()
async def ping(ctx):
    bot_latency = round(client.latency*1000)
    await ctx.send(f"your ping is {bot_latency} ms")



#to send the message in private add .author adter ctx
@client.command()
async def MO(ctx):
    await ctx.send("Monday left me broken!")




#random answer 

@client.command()
async def ask_me(ctx, *, question):
    with open(" \discord\\responses.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
    
    await ctx.send(response)


        

client.run("")



