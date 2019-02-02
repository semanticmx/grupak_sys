# -*- coding: utf-8 -*-
miLista = [34,93,19]

def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        #print (pivote)
        for i in lista:
            #print (f"valor {i}")
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

print(miLista)
print(sort(miLista))