
def ordenamiento_shell(lista):
    """
    Recibe como parametro: lista, y la divide en distintas "sublistas"

    """
    contador_sublistas = len(lista) // 2   # Obtiene la longitud de la lista (Floor), se redondea hacia abajo.

    while contador_sublistas > 0:
        for posicion_inicio in range(contador_sublistas):  # 0 in range(4,2,1)
            brecha_ordenamiento(lista, posicion_inicio, contador_sublistas)  # [],0,4

        contador_sublistas = contador_sublistas // 2  # División tipo (Floor)


def brecha_ordenamiento(lista, inicio, brecha):  # [],0,4
    """
    Recibe como parametros: lista, inicio, brecha; para
    posteriormente comparar y ordenar los elementos de
    cada sublista recibida, de acuerdo al algoritmo siguiente.

    """

    for i in range(inicio + brecha, len(lista), brecha):
        valor_actual = lista[i]
        posicion = i

        while posicion >= brecha and lista[posicion - brecha] > valor_actual:
            lista[posicion] = lista[posicion - brecha]
            posicion = posicion - brecha

        lista[posicion] = valor_actual


if __name__ == '__main__':
    lista_prueba = [54, 26, 93, 17, 77, 31, 44, 55, 20, ]
    ordenamiento_shell(lista_prueba)
    print(lista_prueba)
