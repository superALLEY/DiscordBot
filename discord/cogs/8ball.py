import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
import os
import asyncio

class AskMe(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("8ball.py is ready!")

    @commands.command()
    async def ask_me(self,ctx, *, question):
        with open("\Bureau\\discord\\responses.txt", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)
    
        await ctx.send(response)
    
    

    




async def setup(client):
    await client.add_cog(AskMe(client))