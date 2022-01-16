from urllib import response
import requests

def have_numbers():
    response = requests.get(f'http://challenge.dienekes.com.br/api/numbers?page={100000}').content
    assert response == 200
