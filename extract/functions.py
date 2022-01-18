import requests
import codecs
import json


def extract():
    try:
        numbers = open('numbers.csv', 'w')
        count = 1
        have_numbers = True
        # while have_numbers:
        while count <= 50:
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


def read_numbers():
    numbers = open('numbers.csv')
    return numbers.readlines()
