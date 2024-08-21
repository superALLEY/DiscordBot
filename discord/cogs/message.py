import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
import os
import asyncio

class Message(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("message.py is ready!")
    
    @commands.command()
    async def message(self, ctx):
         await ctx.send(f"Monday left me Broken!")

    








async def setup(client):
    await client.add_cog(Message(client))