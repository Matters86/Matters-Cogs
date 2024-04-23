from .vnetapi import vnetapi


async def setup(bot):
    await bot.add_cog(vnetapi(bot))