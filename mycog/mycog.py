from discord.ext import tasks
from redbot.core import Config, commands
import aiohttp
import json

class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        print('Please wait while Bot started')
        self.bot = bot
        self.config = Config.get_conf(self, identifier=7888, force_registration=True)
        print('Bot ready')
        print('Commands: "hello", "addToken"')

    @commands.command()
    async def hello(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Hello from my Bot!")

    @commands.command()
    async def addToken(self, ctx):
        self.config.set({ 'token_test': 'abcdef'})
        await ctx.send('Add Token')

