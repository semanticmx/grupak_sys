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


if __name__ == '__main__':
    from random import shuffle

    max_items = 20000
    mi_lista = [n for n in range(max_items)]
    shuffle(mi_lista)

    lista_ordenada = quick_sort(mi_lista)
    print(f'Lista: {lista_ordenada}')
