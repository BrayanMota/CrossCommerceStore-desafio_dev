import requests
import codecs
import json

response = requests.get(
    f'http://challenge.dienekes.com.br/api/numbers?page={10000}')
valor = codecs.decode(response.content, 'UTF-8')

outro_valor = json.loads(valor)


if not outro_valor.get('numbers'):
    print('Lista Vazia')
else:
    print('Lista Cheia')
