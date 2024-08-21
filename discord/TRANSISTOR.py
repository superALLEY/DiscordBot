import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
import os
import asyncio
import json

def get_server_prefix(client,message):
    with open ("\discord\\Prefix.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

client = commands.Bot(command_prefix=get_server_prefix,intents=discord.Intents.all())

bot_status = cycle(["Developed By superALLEY","join our server","LINK in bio","Developed By superALLEY","TO game && TO study!!","Developed By superALLEY","stop looking at me","Developed By superALLEY","type in '!help' for help"])   
@tasks.loop(seconds=5)  
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status))) 


client.remove_command("help")


@client.event
async def on_ready():
    await client.tree.sync()
    print("succes: Bot is connected to Discord")
    change_status.start()


#/command
@client.tree.command(name="ping" , description="latency of THE TRANSISTOR's bot in ms")
async def Ping(interaction:discord.Interaction):
    bot_latency=round(client.latency*1000)
    await interaction.response.send_message(f"Bot latency: {bot_latency} ms")


#8ball
@client.tree.command(name="askme" , description="Ask our bot!..He will answer!")
async def AskMe(interaction:discord.Interaction):
        with open(" \discord\\responses.txt", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)
        await interaction.response.send_message(response)


#message

@client.tree.command(name="mo" , description="that cat is here")
async def MO(interaction:discord.Interaction):
        await interaction.response.send_message("Monday left me broken!") 

        



        
#mute/unmute

@client.event
async def on_guild_join(guild):
    with open(" \discord\\cogs\\jsonfiles\\mutes.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role[str(guild.id)] = None
    
    with open(" \discord\\cogs\\jsonfiles\\mutes.json", "w") as f:
        json.dump(mute_role, f, indent=4)
 
@client.event
async def on_guild_remove(guild):
    with open(" \discord\\cogs\\jsonfiles\\mutes.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role.pop(str(guild.id))
    
    with open(" \discord\\cogs\\jsonfiles\\mutes.json", "w") as f:
        json.dump(mute_role, f, indent=4)
    












#to set a prefix !change_prefix = 
@client.event
async def on_guild_join(guild):
    with open (" \discord\\Prefix.json", "r") as f:
        prefix = json.load(f)

    prefix[str(guild.id)] = "!"

    with open (" \discord\\Prefix.json", "w") as f:
        json.dump(prefix, f , indent=4)
    


@client.event
async def on_guild_remove(guild):
    with open (" \discord\\Prefix.json", "r") as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

    with open (" \discord\\Prefix.json", "w") as f:
        json.dump(prefix, f , indent=4)

@client.command()
async def change_prefix(ctx, *,newprefix: str):
    with open (" \discord\\Prefix.json", "r") as f:
        prefix = json.load(f)

    prefix[str(ctx.guild.id)] = newprefix

    with open (" \discord\\Prefix.json", "w") as f:
        json.dump(prefix, f , indent=4)














#autorole


@client.event
async def on_guild_join(guild):
    with open(" \discord\\cogs\\jsonfiles\\Roles.json","r") as f:
        auto_role = json.load(f)

    auto_role[str(guild.id)] = None

    with open(" \discord\\cogs\\jsonfiles\\Roles.json","w") as f:
        json.dump(auto_role, f ,indent=4)

@client.event
async def on_guild_remove(guild):
    with open(" \discord\\cogs\\jsonfiles\\Roles.json","r") as f:
        auto_role = json.load(f)

    auto_role.pop(str(guild.id))

    with open(" \discord\\cogs\\jsonfiles\\Roles.json","w") as f:
        json.dump(auto_role, f ,indent=4)
    



    


#welcome

@client.event
async def on_guild_join(guild):
    with open(" \discord\\cogs\\jsonfiles\\welcome.json","r") as f:
        data = json.load(f)

    data[str(guild.id)]={}
    data[str(guild.id)]["Channel"] = None
    data[str(guild.id)]["Message"] = None
    data[str(guild.id)]["AutoRole"]= None
    data[str(guild.id)]["imageUrl"]= None

    with open(" \discord\\cogs\\jsonfiles\\welcome.json","w") as f:
        json.dump(data, f ,indent=4)
        
@client.event
async def on_guild_remove(guild):
    with open(" \discord\\cogs\\jsonfiles\\welcome.json","r") as f:
        data = json.load(f)

    data.pop(str(guild.id))



    with open(" \discord\\cogs\\jsonfiles\\welcome.json","w") as f:
        json.dump(data, f ,indent=4)






#banned words


#autorole button

class SelfRoles(discord.ui.View):
    def __init__ (self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Red", style=discord.ButtonStyle.red)
    async def red_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        red_role = discord.utils.get(interaction.guild.roles, name="Red team")            
        await interaction.user.add_roles(red_role)

    @discord.ui.button(label="Green",style=discord.ButtonStyle.green)
    async def green_color(self, interaction: discord.Interaction, Button: discord.ui.Button):
        green_role = discord.utils.get(interaction.guild.roles, name="Green team")
        await interaction.user.add_roles(green_role)

    @discord.ui.button(label="Blurple", style=discord.ButtonStyle.blurple)
    async def blurple_color(self, interaction: discord.Interaction, Button: discord.ui.Button): 
        blurple_role = discord.utils.get(interaction.guild.roles, name="Blurple team")
        await interaction.user.add_roles(blurple_role)




@client.tree.command(name="selfroles", description="Give yourself a neat and colorfule role!")
async def self_role(interaction: discord. Interaction):
     await interaction.response.send_message(content="Click a button corosponding to the role color you want!", view=SelfRoles())


#setcolor
class SelectMenu(discord.ui.View):
        options = [
            discord.SelectOption(label="Red", value="1", description="Gives the color red to user."), 
            discord.SelectOption(label="Blue", value="2", description="Gives the color blue to user."), 
            discord.SelectOption(label="yellow", value="3", description="Gives the color yellow to user.")
        ]
    
        @discord.ui.select(placeholder="Select Color", options=options)
        async def menu_callback(self, interaction: discord.Interaction, select):
            select.disabled=True
            if select.values[0] == "1":
            
                 await interaction.response.send_message(content="vour color is now red.")
            elif select.values[0] == "2":
            
                await interaction.response.send_message(content="Your color is now blue.")
            elif select.values[0] == "3":
            
                await interaction.response.send_message(content="Your color is now yellow.")
@client.tree.command(name="setcolor", description="Sets your role color of choice.")
async def setcolor(interaction: discord.Interaction):
    await interaction.response.send_message(content="Select your role color!", view=SelectMenu())


#report





class ReportModal(discord.ui.Modal, title="Report user"):

    user_name = discord.ui.TextInput(label="User's Discord Name", placeholder="eg. JohnDoe#0000", required=True, max_length=100, style=discord.TextStyle.short)
    user_id = discord.ui.TextInput(label="User's Discord ID", placeholder="To grab a user's ID, make sure Developer Mode is on.", required=True, max_length=100, style=discord.TextStyle.short) 
    description = discord.ui.TextInput(label="What did they do?", placeholder="eg. Broke rule #7", required=True, min_length=200, max_length=2000, style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} Thank you for submitting your report, the moderation team will see it momentarily!", ephemeral=True)
        channel = discord.utils.get(interaction.guild.channels, name="mod")
        await channel.send(f"Report Submitted by {interaction.user.mention} \n Name: {self.user_name} \n ID: {self.user_id} \n Reported For: {self.description}")
@client.tree.command(name="report", description="Report a user") 
async def report(interaction: discord.Interaction):
    await interaction.response.send_modal(ReportModal())


async def load():
    for filename in os.listdir(" \discord\\cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            

async def main():
    async with client:
        await load()
        await client.start("")   
        

asyncio.run(main())










