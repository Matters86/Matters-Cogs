import aiohttp
import asyncio
import json

async def push():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.restful-api.dev/objects') as response:
            html = await response.text()
            myObject = json.loads(html)
            
            print(myObject[1]['name'])
            

asyncio.run(push())