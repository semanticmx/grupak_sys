class Shell():

    # def _init_(self,tipo):
    #
    #     self.tipo=tipo
    #     print(self.tipo)
    # def ordenamientoShell(self):
    #
    #
    ####################################################################################################################

    def brecha_ordenamiento(unaLista,inicio,brecha): #[],0,4

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

            #return unaLista[posicion]
    ####################################################################################################################

    def ordenamiento_shell(list):

        """
            Recibe como parametro: unaLista, y la divide en distintas "sublistas"
        """
        contadorSublistas = len(list) // 2  # Obtiene la longitud de la lista (Floor), se redondea hacia abajo.

        while contadorSublistas > 0:

            for posicionInicio in range(contadorSublistas):  # 0 in range(4,2,1)

                #brecha_ordenamiento(unaLista, posicionInicio, contadorSublistas)  # [],0,4

                print("Dividiendo en sublista:", contadorSublistas,
                      "La lista es", list)

        contadorSublistas = contadorSublistas // 2  # División tipo (Floor)

    ####################################################################################################################


#ordenador=Shell(tipo="Shell") #Objeto
#ordenador.ordenamientoShell() #Funcion
unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20, ]
ordenador=Shell()
ordenador.ordenamiento_shell(unaLista)
