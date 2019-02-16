"""
Ordenamiento HeapSort

"""


def swap(a, i, j):
    """
    intercambia valores del arreglo a, en las posiciones i y j

    """
    a[int(i)], a[int(j)] = a[int(j)], a[int(i)]


def is_heap(a):
    """
    checa si los dos elementos del arreglo son un heap

    """
    n = 0
    m = 0
    # ciclo infinito, se rompe cuando alguna de las dos condiciones se cumple (líneas 29 y 31)
    while True:
        for i in range(1):
            m += 1
            if m >= len(a):
                return True
            if a[m] > a[n]:
                return False
        n += 1


def shift_down(a, n, maximo):
    """
    ordena los pares de a, hasta maximo

    """
    while True:
        biggest = n
        c1 = 2 * n + 1
        c2 = c1 + 1

        for c in [int(c1), int(c2)]:
            if c < maximo and a[int(c)] > a[int(biggest)]:
                biggest = c

        if biggest == n:
            return
        swap(a, n, biggest)
        n = biggest


def heapify(a):
    """
    ordena la lista en pares.

    """
    i = len(a) / 2 - 1
    maximo = len(a)
    while i >= 0:
        shift_down(a, i, maximo)
        i -= 1


def heapsort(a):
    """
    inicia ordenamiento heapsort de a

    """
    heapify(a)
    j = len(a) - 1
    while j > 0:
        swap(a, 0, j)
        shift_down(a, 0, j)
        j -= 1

    return a


if __name__ == '__main__':
    lista = [54, 26, 93, 17, 77, 31, 44, 55, 20, ]
    heapsort(lista)
    print(lista)
