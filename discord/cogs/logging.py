import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
import os
import asyncio

class Events(commands.Cog):
    def	__init__(self, client): 
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Events.py is online.")

   
    @commands.Cog.listener()
    async def on_member_join(self,member):
        log_channel = discord.utils.get(member.guild.channels, name="logs")
        event_embed = discord.Embed(title="Arrival Logged", description="This user landed in the server!", color=discord.Color.green()) 
        event_embed.add_field(name="User Joined:", value=member.mention, inline=False)
        await log_channel.send(embed=event_embed)

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        log_channel = discord.utils.get(member.guild.channels, name="logs")
        event_embed = discord.Embed(title="Departure Logged", description="This user left the server!", color=discord.Color.green()) 
        event_embed.add_field(name="user Left:", value=member.mention, inline=False)
        await log_channel.send(embed=event_embed)

async def setup(client):
    await client.add_cog(Events(client))