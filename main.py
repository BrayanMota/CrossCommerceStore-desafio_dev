
lista1 = [12, 14, 6, 32, 9, 0, 1, 24, 8, 14]

lista2 = []
for numero in lista1:
    for chave, valor in enumerate(lista2):
        print(chave, valor)
        if numero < valor:
            lista2.insert(chave, numero)
            break
    else:
        lista2.append(numero)
    print("Lista atual:", lista2)
