from redbot.core import commands
import aiohttp
import json

class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        self.show.start()

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    from discord.ext import tasks

    @tasks.loop(seconds=30)
    async def show(self, ctx):
        await ctx.send("I can do stuff!")


    @commands.command()
    async def push(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.restful-api.dev/objects') as response:
                html = await response.text()
                myObject = json.loads(html)
                await ctx.send(myObject[1]['name'])
