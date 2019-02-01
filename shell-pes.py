unaLista = [54,26,93,17,77,31,44,55,20,]

def ordenamientoDeShell(unaLista):

    """
        Recibe como parametro: unaLista, y la divide en distintas "sublistas"
    """

    contadorSublistas = len(unaLista)//2   #Obtiene la longitud de la lista (Floor), se redondea hacia abajo.

    while contadorSublistas > 0:

      for posicionInicio in range(contadorSublistas):  #0 in range(4,2,1)

        brechaOrdenamientoPorInsercion(unaLista,posicionInicio,contadorSublistas) #[],0,4

        print("Dividiendo en sublista:",contadorSublistas,
                                        "La lista es",unaLista)

    contadorSublistas = contadorSublistas // 2  #División tipo (Floor)

def brechaOrdenamientoPorInsercion(unaLista,inicio,brecha): #[],0,4

    """
        Recibe como parametros: unaLista, inicio, brecha; para
        posteriormente comparar y ordenar los elementos de cada sublista recibida, de acuerdo al algoritmo siguiente.
    """

    for i in range(inicio+brecha,len(unaLista),brecha):

        valorActual = unaLista[i]
        posicion = i

        while posicion>=brecha and unaLista[posicion-brecha]>valorActual:

            unaLista[posicion]=unaLista[posicion-brecha]

            posicion = posicion-brecha

        unaLista[posicion]=valorActual


ordenamientoDeShell(unaLista)
print(unaLista)