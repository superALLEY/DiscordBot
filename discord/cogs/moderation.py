import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
import os
import asyncio
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print("Moderation.py is ready!")
    








  





    



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx , count: int):
        await ctx.channel.purge(limit=count)
        await ctx.send(f"{count} message(s) has/have been deleted.")
       









    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx , member: discord.Member, *, modreason):
        await ctx.guild.kick(member)

        conf_embed = discord.Embed(title="succes!",color=discord.Color.green())
        conf_embed.add_field(name="kicked:" , value=f"{member.mention} has been kicked from the server by {ctx.author.mention}.",inline=False)
        conf_embed.add_field(name="Reason:", value=modreason,inline=False)

        await ctx.send(embed=conf_embed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx , member: discord.Member, *, modreason):
        await ctx.guild.ban(member)

        conf_embed = discord.Embed(title="succes!",color=discord.Color.green())
        conf_embed.add_field(name="banned:" , value=f"{member.mention} has been banned from the server by {ctx.author.mention}.",inline=False)
        conf_embed.add_field(name="Reason:", value=modreason,inline=False)

        await ctx.send(embed=conf_embed)

#to unban you use the id of the user not the @
    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self , ctx , userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)

        conf_embed = discord.Embed(title="succes!",color=discord.Color.green())
        conf_embed.add_field(name="unbanned:" , value=f"<@{userId}> has been unbanned from the server by {ctx.author.mention}.",inline=False)
        

        await ctx.send(embed=conf_embed)
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error : Missing required Arguments. you must give a number of how many messages to clear.")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error : Missing required Arguments. you must @ or give THE ID of the user you want to ban .")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error : Missing required Arguments. you must @ or give THE ID of the user you want to unban.")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error : Missing required Arguments. you must @ or give THE ID of the user you want to kick.")

    

        



async def setup(client):
    await client.add_cog(Moderation(client))