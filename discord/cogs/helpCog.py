import discord
from discord.ext import commands
import json
import random


class HelpCO(commands.Cog):
    def __init__(self,client) :
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Help.py is ready.")

    @commands.command()
    async def help(self, ctx):

        help_embed = discord.Embed(title="Help Desk for TRANSISTOR",description="you will find all the commands here.",color=discord.Color.random())
        help_embed.set_author(name="TRANSISTOR")

        help_embed.add_field(name="clear",             value=  "deletes a specific amounts of messages 'admins only'"         ,inline=False)
        help_embed.add_field(name="ask_me",            value="8ball game answers your YES/NO Q"                               ,inline=False)
        help_embed.add_field(name="ping",              value="Shows bot's ping 'admins only'"                                 ,inline=False)
        help_embed.add_field(name="change_prefix",     value="Changes the prefix of the commands admins only'"                ,inline=False)
        help_embed.add_field(name="ban",               value="bans a specific membber 'admins only'"                          ,inline=False)
        help_embed.add_field(name="unban",             value="unbans a specific membber 'admins only'"                        ,inline=False)
        help_embed.add_field(name="kick",              value="kicks a specific membber 'admins only'"                         ,inline=False)
        help_embed.add_field(name="mute",              value="gives the muted role to a specific member 'admins only'"        ,inline=False)
        help_embed.add_field(name="unmute",            value="removes the muted role to a specific member 'admins only'"      ,inline=False)
        help_embed.add_field(name="setmtuerole",       value="gves the muted role to a specific role 'admins only'"           ,inline=False)
        help_embed.add_field(name="message",           value="Sends u a surprise 'admins only'"                               ,inline=False)
        help_embed.add_field(name="embed",             value="a tool to send emebd messages 'admins only'"                    ,inline=False)
        help_embed.add_field(name="joinrole",          value="set the join role of the server 'admins only'"                  ,inline=False)
        help_embed.add_field(name="level",             value="shows users level "                                             ,inline=False)
        help_embed.add_field(name="lvl",               value="shows users level "                                             ,inline=False)
        help_embed.add_field(name="Need help?",        value="[Join The support server!](https://discord.gg/yD7rWgy7jH)"   ,inline=False)

        help_embed.set_footer(text=f"Requested by <@{ctx.author}>.",icon_url=ctx.author.avatar)

        await ctx.send(embed = help_embed)
    

async def setup(client):
    await client.add_cog(HelpCO(client))

    