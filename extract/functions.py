import requests
import codecs
import json
import asyncio
import aiohttp
import time
import os


def extract():
    try:
        numbers = open('numbers.csv', 'w')
        count = 1
        have_numbers = True
        while have_numbers:
            list_numbers = []
            response = requests.get(
                f'http://challenge.dienekes.com.br/api/numbers?page={count}')
            response_str = codecs.decode(response.content, 'UTF-8')
            numbers_dic = json.loads(response_str)

            print(f'Page: {count}')
            if not numbers_dic.get('numbers'):
                if response.status_code == 500:
                    print(f'Page interruped: {count}')
                    continue
                else:
                    print('Empty page')
                    have_numbers = False

            list_numbers.extend(numbers_dic.get('numbers'))
            for number in list_numbers:
                numbers.write(f'{str(number)}\n')
            count += 1

        numbers.close()

        return read_numbers()
    except Exception as e:
        raise e


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
        raise f'{url} - {e}'


async def main():
    start = time.time()
    pages = 1000
    if os.path.exists('numbers.csv'):
        os.remove('numbers.csv')
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[get(f'http://challenge.dienekes.com.br/api/numbers?page={page+1}', session) for page in range(pages)])
        while page_errors:
            await asyncio.gather(*[get(page, session) for page in page_errors])
    end = time.time()
    return f'Took {end - start} seconds to take all numbers.'
