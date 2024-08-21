import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
import os
import asyncio
from discord import app_commands

class userinfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("userinfo.py is ready!")

    @app_commands.command(name="userinfo",description="sends user's informations(sends own if none)")
    async def avatar(self,interaction: discord.Interaction,member: discord.Member=None): 
        if member is None:
            member = interaction.user
        elif member is not None:
            member = member
        info_embed = discord.Embed(title=f"{member.name}'s User Information", color=discord.Color.random())
        info_embed.set_image(url=member.avatar)
        info_embed.add_field(name="Name:", value=interaction.user.name, inline=False)
        info_embed.add_field(name="Nick Name:", value=interaction.user.display_name, inline=False)
        info_embed.add_field(name="Discriminator:", value=interaction.user.discriminator, inline=False)
        info_embed.add_field(name="ID:", value=interaction.user.id, inline=False)
        info_embed.add_field(name="Top Role:", value=interaction.user.top_role, inline=False)
        info_embed.add_field(name="Status:", value=interaction.user.status, inline=False)
        info_embed.add_field(name="Bot User?", value=interaction.user.bot, inline=False)
        info_embed.add_field(name="Creation Date:", value=interaction.user.created_at.__format__("%A, %d. %B %Y @ %H:%M:%S"), inline=False)

        await interaction.response.send_message(embed=info_embed)
    
    

    




async def setup(client):
    await client.add_cog(userinfo
(client))