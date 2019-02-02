from random import shuffle
from time import time

max_items = 20000
mi_lista = [n for n in range(max_items)]
shuffle(mi_lista)


def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return sort(izquierda)+centro+sort(derecha)
    else:
        return lista


start_time = time()
lista_ordenada = sort(mi_lista)
stop_time = time()

print(f'Lista: {lista_ordenada}, ordenada en {stop_time - start_time}')
