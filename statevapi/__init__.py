from .statevapi import statevapi


async def setup(bot):
    await bot.add_cog(statevapi(bot))