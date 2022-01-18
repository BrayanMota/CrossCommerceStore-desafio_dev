import requests
import codecs
import json
import time


def extract():
    try:
        numbers = open('numbers.csv', 'w')
        count = 1
        # while True:
        while count <= 100:
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
                    break

            list_numbers.extend(numbers_dic.get('numbers'))
            for number in list_numbers:
                numbers.write(f'{str(number)}\n')
            count += 1

            # Controle the time of requisitions
            # time.sleep(1)
        numbers.close()

        numbers = open('numbers.csv')
        return numbers.readlines()
        # return 'All pages copied'
    except Exception as e:
        raise e
