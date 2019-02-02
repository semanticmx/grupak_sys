from random import shuffle
from time import time

max_items = 20000
mi_lista = [n for n in range(max_items)]
shuffle(mi_lista)


def quick_sort(lista):
    """
    implementación del método de ordenamiento quick sort.
    compara 3 listas y las concatena, de manera recursiva.

    """
    izquierda, centro, derecha = [], [], []

    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return quick_sort(izquierda) + centro + quick_sort(derecha)
    else:
        return lista


start_time = time()
lista_ordenada = quick_sort(mi_lista)
stop_time = time()

print(f'Lista: {lista_ordenada}, ordenada en {stop_time - start_time}')
