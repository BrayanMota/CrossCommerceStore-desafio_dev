import os


def transform():
    try:
        numbers = open('numbers.csv', 'r')
        numbers_in_order = open('numbers_in_order.csv', 'w')
        lista = []
        i = 1
        for number in numbers:
            print(f'Number {number}')
            for key, value in enumerate(lista):
                if number < value:
                    lista.insert(key, number)
                    break
            else:
                lista.append(number)

        for number in lista:
            numbers_in_order.write(f'{str(number)}')
        return 'All numbers sorted'
    except Exception as e:
        raise e
