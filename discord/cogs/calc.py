import discord
from discord.ext import commands 
from numpy import *
import numexpr

class Calc(commands.Cog):
    def __init__ (self, client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online.")

    @commands.command(aliases=["calc", "solve"])
    async def calculate(self, ctx, *, expression: str):
        try:
            answer = numexpr.evaluate(expression)
            await ctx.send(f"{expression} = {answer}") 
        except:
            await ctx.send("Error: Invalid Expression.")
async def setup(client):
    await client.add_cog(Calc(client))