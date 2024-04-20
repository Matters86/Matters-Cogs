from redbot.core import commands, tasks
#from discord.ext import tasks
import aiohttp
import json

class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        print('Start system')
        self.bot = bot
        self.counter = 0
        self.show.start()

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @tasks.loop(seconds=30)
    async def show(self):
        print(self.counter)
        self.counter += 1


    @commands.command()
    async def push(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.restful-api.dev/objects') as response:
                html = await response.text()
                myObject = json.loads(html)
                await ctx.send(myObject[1]['name'])
