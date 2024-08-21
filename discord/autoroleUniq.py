import discord
from discord.ext import commands
import json
import random

#local method
class Auto(commands.Cog):
    def __init__(self,client) :
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("autoRole.py is ready.")

    @commands.Cog.listener()
    async def on_member_join(self, member):

        
        join_role = discord.utils.get(member.guild.roles,name="「🌍」Community")

        await member.add_roles(join_role)

async def setup(client):
    await client.add_cog(Auto(client))

     #cog file