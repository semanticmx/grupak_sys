def ordenamiento_insercion(lista_n):
    """
    implementación del ordenamiento de inserción

    """
    for i in range(len(lista_n)):
        minimo = i

        for j in range(i, len(lista_n)):
            if lista_n[j] < lista_n[minimo]:
                minimo = j
        if minimo != i:
            lista_n[i], lista_n[minimo] = lista_n[minimo], lista_n[i]

    return lista_n


if __name__ == '__main__':
    lista_prueba = [6, 5, 3, 1, 8, 7, 2, 4, ]
    print(ordenamiento_insercion(lista_prueba))
