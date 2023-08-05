import os
import aiohttp
import aiofiles


async def save_file(url: str, file_location_name='./cover.jpg'):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(file_location_name, mode='wb')
                await f.write(await resp.read())
                await f.close()
    return file_location_name


def delete_file(file_location='./cover.jpg'):
    os.remove(file_location)
