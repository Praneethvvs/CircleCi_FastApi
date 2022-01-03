import asyncio

import aiohttp
from general_dir.Thread_test import Time_Detector

import time

URL = 'https://httpbin.org/uuid'


async def fetch(session, url):
    print(1)
    async with session.get(url) as response:
        json_response = await response.json()
        print(json_response['uuid'])



async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL) for _ in range(100)]
        await asyncio.gather(*tasks)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@Time_Detector
def execute_this():
    asyncio.run(main())

# execute_this()
