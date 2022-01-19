import codecs
import json
import asyncio
import aiohttp
import time
import os


page_errors = []


async def get(url, session):
    try:
        async with session.get(url=url) as response:
            resp = await response.read()
            response_str = codecs.decode(resp, 'UTF-8')
            numbers_dic = json.loads(response_str)

            if not numbers_dic.get('error'):
                numbers = open('numbers.csv', 'a')
                list_numbers = []

                list_numbers.extend(numbers_dic.get('numbers'))
                for number in list_numbers:
                    numbers.write(f'{str(number)}\n')
                    
                numbers.close()

                if url in page_errors:
                    page_errors.remove(url)
            else:
                page_errors.append(url)

    except Exception as e:
        raise f'{url} - e'


async def main():
    pages = 10000
    if os.path.exists('numbers.csv'):
        os.remove('numbers.csv')
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[get(f'http://challenge.dienekes.com.br/api/numbers?page={page+1}', session) for page in range(pages)])
        while page_errors:
            await asyncio.gather(*[get(page, session) for page in page_errors])
    print("Finalized all.")


start = time.time()
asyncio.run(main())
end = time.time()

print(f'Took {end - start} seconds to pull websites.')
