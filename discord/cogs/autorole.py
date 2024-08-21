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

        with open("\discord\\cogs\\jsonfiles\\Roles.json","r") as f:
            auto_role = json.load(f)

        
        join_role = discord.utils.get(member.guild.roles,name=auto_role[str(member.guild.id)])

        await member.add_roles(join_role)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def joinrole(self, ctx , role:discord.Role):
        with open("\discord\\cogs\\jsonfiles\\Roles.json","r") as f:
            auto_role = json.load(f)

        auto_role[str(ctx.guild.id)]=str(role.name)
        with open("\discord\\cogs\\jsonfiles\\Roles.json","w") as f:
            json.dump(auto_role, f ,indent=4)

        conf_embed=discord.Embed(color=discord.Color.blue())
        conf_embed.add_field(name="Succes!",value=f"auto role for this server has been set to{role.mention}.")
        conf_embed.set_footer(text=f"BY {ctx.author.name}.") 

        await ctx.send(embed=conf_embed)       




async def setup(client):
    await client.add_cog(Auto(client))

    
