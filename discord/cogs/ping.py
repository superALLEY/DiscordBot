import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
import os
import asyncio

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready!")
    
    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency*1000)
        await ctx.send(f"haha your ping is {bot_latency} ms ")



async def setup(client):
    await client.add_cog(Ping(client))









