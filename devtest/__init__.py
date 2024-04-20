from .devtest import devtest


async def setup(bot):
    await bot.add_cog(devtest(bot))