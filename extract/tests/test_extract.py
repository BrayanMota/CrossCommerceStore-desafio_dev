import requests
import codecs
import json
import random


def test_extract_200():
    response = requests.get('http://challenge.dienekes.com.br/api/numbers')
    assert response.status_code == 200


def test_extract_with_page_200():
    page = random.randint(1, 10000)
    response = requests.get(
        f'http://challenge.dienekes.com.br/api/numbers?page={page}')
    assert response.status_code == 200


def test_extract_404():
    response = requests.get('http://challenge.dienekes.com.br/api/number')
    assert response.status_code == 404


def test_extract_no_numbers():
    response = requests.get(
        f'http://challenge.dienekes.com.br/api/numbers?page={10001}')
    response_str = codecs.decode(response.content, 'UTF-8')
    numbers_dic = json.loads(response_str)

    assert numbers_dic.get('numbers') == []


# TODO Arrumar para funcionar o teste
# def test_extract_handling_error_500():
#     count = 1
#     simulated_error = False
#     while count <= 100 or simulated_error == True:
#         response = requests.get(
#             f'http://challenge.dienekes.com.br/api/numbers?page={count}')

#         print(f'Page: {count}')
#         if response.status_code == 500:
#             print(f'Page Interruped: {count}')
#             simulated_error == True
#         count += 1

#     assert response.status_code == 500
