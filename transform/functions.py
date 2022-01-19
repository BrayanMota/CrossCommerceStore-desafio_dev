import time


def quick_sort(lista):

    list_greatest = []
    list_minors = []

    if len(lista) <= 1:
        return lista

    pivo = lista.pop()

    # Using list comprehension
    # [list_minors.append(item) if item < pivo else list_greatest.append(item) for item in lista]
    
    # Optei por não utilizar dessa forma, pois em testes feitos na minha máquina, teve uma certa diferença de
    # tempo para a ordenação de todos os valores.

    for item in lista:
        if item < pivo:
            list_minors.append(item)
        else:
            list_greatest.append(item)

    return quick_sort(list_minors) + [pivo] + quick_sort(list_greatest)


def transform():
    try:
        lista = []
        with open('numbers.csv', 'r') as numbers:
            for number in numbers:
                lista.append(number)

        start = time.time()
        values = quick_sort(lista)
        end = time.time()

        with open('numbers_in_order.csv', 'w') as numbers_in_order:
            for value in values:
                numbers_in_order.write(f'{str(value)}')

        return f'Took {end - start} seconds to sort all numbers.'
    except Exception as e:
        raise e
