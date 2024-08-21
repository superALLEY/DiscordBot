import discord
from discord.ext import commands
import json
import random

#local method
class welcome(commands.Cog):
    def __init__(self,client) :
        self.client = client

        


    @commands.Cog.listener()
    async def on_ready(data):
        print("welcome.py is ready.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open(" \discord\\cogs\\jsonfiles\\welcome.json","r") as f:
            data = json.load(f)


        welcome_embed=discord.Embed(title=f"everyone ! a new member for {member.guild.name}!", description=f"member number {member.guild.member_count} is here!",color=discord.Color.purple())
       
        welcome_embed.add_field(name="Welcome to the server!", value=data[str(member.guild.id)]["Message"], inline=False)
        welcome_embed.set_image(url=data[str(member.guild.id)]["imageUrl"])
        welcome_embed.set_footer(text="glad you've joined!", icon_url=member.avatar)

        auto_role = discord.utils.get(member.guild.roles, name=data[str(member.guild.id)]["AutoRole"])

        await member.add_roles(auto_role)
        
        if data[str(member.guild.id)]["Channel"] is None:
            await member.send(embed=welcome_embed)
        elif data[str(member.guild.id)]["Channel"] is not None:

            welcome_channel = discord.utils.get(member.guild.channels, name=data[str(member.guild.id)]["Channel"])

            await welcome_channel.send(embed=welcome_embed)

    @commands.group(name="welcome",invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def welcome(self, ctx):

        info_embed=discord.Embed(title="Welcome setup",description="create a welcome system for your server!",color=discord.Color.teal())
        info_embed.add_field(name="autorole",value="set an autotmatic role so when a member join will get it automatically",inline=False)
        info_embed.add_field(name="message",value="set a message to be included in your Welcome card",inline=False)
        info_embed.add_field(name="channel",value="set a channel for your Welcome card",inline=False)
        info_embed.add_field(name="img",value="set an image for your welcome card",inline=False)
        
        await ctx.send(embed=info_embed)





    @welcome.command()
    @commands.has_permissions(administrator=True)
    async def autorole(self, ctx , role: discord.Role):
        with open(" \discord\\cogs\\jsonfiles\\welcome.json","r") as f:
            data = json.load(f)
        data[str(ctx.guild.id)]["AutoRole"]=str(role.name)

        with open(" \discord\\cogs\\jsonfiles\\welcome.json","w") as f:
            json.dump(data , f ,indent=4)



        


    @welcome.command()
    @commands.has_permissions(administrator=True)
    async def message(self, ctx , *, msg):
        with open(" \discord\\cogs\\jsonfiles\\welcome.json","r") as f:
            data = json.load(f)
        data[str(ctx.guild.id)]["Message"]=str(msg)

        with open(" \discord\\cogs\\jsonfiles\\welcome.json","w") as f:
            json.dump(data , f,indent=4)






    @welcome.command()
    @commands.has_permissions(administrator=True)
    async def channel(self, ctx , channel: discord.TextChannel):
        with open(" \discord\\cogs\\jsonfiles\\welcome.json","r") as f:
            data = json.load(f)
        data[str(ctx.guild.id)]["Channel"]=str(channel.name)

        with open(" \discord\\cogs\\jsonfiles\\welcome.json","w") as f:
            json.dump(data , f ,indent=4)






    @welcome.command()
    @commands.has_permissions(administrator=True)
    async def img(self, ctx , *, url):

        with open(" \discord\\cogs\\jsonfiles\\welcome.json","r") as f:
            data = json.load(f)
        data[str(ctx.guild.id)]["imageUrl"]=str(url)

        with open(" \discord\\cogs\\jsonfiles\\welcome.json","w") as f:
            json.dump(data , f ,indent=4)
    




   

async def setup(client):
    await client.add_cog(welcome(client))
