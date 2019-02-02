mi_lista = [34, 93, 19, ]


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
        print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
        return lista


print(mi_lista)
print(sort(mi_lista))
