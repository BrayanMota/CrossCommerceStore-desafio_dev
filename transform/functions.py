numbers = open('numbers.csv', 'r')
numbers_in_order = open('numbers_in_order.csv', 'w')

lista = []
for number in numbers:
    for key, value in enumerate(lista):
        if number < value:
            lista.insert(key, number)
            break
    else:
        lista.append(number)

for number in lista:
    numbers_in_order.write(f'{str(number)}')
