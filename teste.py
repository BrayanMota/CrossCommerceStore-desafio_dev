import asyncio
import codecs
import json
import aiohttp
import time
import base64

websites = """http://challenge.dienekes.com.br/api/numbers"""


async def get(url, session):
    try:
        async with session.get(url=url) as response:
            resp = await response.read()

            response_str = codecs.decode(resp, 'UTF-8')
            numbers_dic = json.loads(response_str)


            print("Successfully got url {} with resp of length {}.".format(
                url, numbers_dic))
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


async def main(urls):
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*[get(url, session) for url in urls])
    print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))


urls = websites.split("\n")
start = time.time()
asyncio.run(main(urls))
end = time.time()

print("Took {} seconds to pull {} websites.".format(end - start, len(urls)))
