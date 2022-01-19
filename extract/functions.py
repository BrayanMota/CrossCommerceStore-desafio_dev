import requests
import codecs
import json
import asyncio
import aiohttp
import time
import os

page_errors = []


async def extract(url, session):
    try:
        async with session.get(url=url) as response:
            resp = await response.read()
            response_str = codecs.decode(resp, 'UTF-8')
            numbers_dic = json.loads(response_str)

            if url in page_errors:
                page_errors.remove(url)

            if not numbers_dic.get('error'):
                with open('numbers.csv', 'a') as numbers:
                    list_numbers = []

                    list_numbers.extend(numbers_dic.get('numbers'))
                    for number in list_numbers:
                        numbers.write(f'{str(number)}\n')
            else:
                page_errors.append(url)

    except Exception as e:
        raise e


async def main():
    pages = 10000
    if os.path.exists('numbers.csv'):
        os.remove('numbers.csv')
    start = time.time()
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[extract(f'http://challenge.dienekes.com.br/api/numbers?page={page+1}', session) for page in range(pages)])
        while page_errors:
            await asyncio.gather(*[extract(page, session) for page in page_errors])
    end = time.time()
    return f'Took {end - start} seconds to take all numbers.'
