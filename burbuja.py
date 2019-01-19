# ordenamiento burbuja
#
# demostrar uso de tipos de datos, utilizando como
# ejemplo el ordenamiento burbuja.
#


# list
lista = [54, 26, 93, 17, 77, 31, 44, 55, 20, ]


def ordenamiento_burbuja(una_lista):
    """
    genera una lista de índices descendentes basados en el tamaño de una_lista - 1
    ie.
        una_lista = [8, 5, 1]
        range => 2, 1
    Compara el primer elemento de la lista, con el elemento n+1
    Si el elemento es mayor, lo intercambia.

    >>> ordenamiento_burbuja([8, 5, 1])
    1, 5, 8
    >>> ordenamiento_burbuja([8])
    8
    >>> ordenamiento_burbuja([])
    'Se espera una lista de números.'
    >>> ordenamiento_burbuja()
    'Argumento incorrecto.'
    >>> ordenamiento_burbuja('Hola')
    'Halo'
    >>> ordenamiento_burbuja('Hola', 1)
    'Argumento incorrecto.'

    """
    # comprehensions
    # for numero in lista:
    #     if numero > 50:
    #         print(numero)

    # list comprehension
    num_mayores_a_50 = [numero for numero in lista if numero > 50]
    print(num_mayores_a_50)

    for num_pasada in range(len(una_lista)-1, 0, -1):
        for i in range(num_pasada):
            if una_lista[i] > una_lista[i+1]:
                una_lista[i], una_lista[i+1] = una_lista[i+1], una_lista[i]


# bases = [2, 4, 6, 8, 10, ]
#
# potencias_al_cuadrado = [x * 2 for x in bases]
#
# print(potencias_al_cuadrado)

ordenamiento_burbuja(lista)
print(lista)
