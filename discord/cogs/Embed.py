import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
import os
import asyncio

class EMbed(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("embed.py is ready!")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def embed(self, ctx):
        embed_message = discord.Embed(title="title of embed" , description="Description of Embed"  ,color=discord.Color.green())
        
        embed_message.set_author(name=f"requested by {ctx.author.mention}", icon_url=ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="Field name", value="Field value",inline=False)
        embed_message.set_footer(text="this is the footer" , icon_url=ctx.author.avatar)

        await ctx.send(embed = embed_message)


async def setup(client):
    await client.add_cog(EMbed(client))