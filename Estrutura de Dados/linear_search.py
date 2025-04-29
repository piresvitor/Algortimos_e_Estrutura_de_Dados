def busca(lista, elem):
    """Returna o indice do elem se ele estiver na lista ou None, caso contrario"""
    for i in range(len(lista)):
        if elem == lista[i]:
            return i
    return None


lista_teste = [1, 4, 3, "python", 5, 6, 7, "7", 8, 2]
elemento = 5

indice = busca(lista_teste, elemento)
if indice is not None:
    print("O indice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não se encontra na lista".format(elemento))
