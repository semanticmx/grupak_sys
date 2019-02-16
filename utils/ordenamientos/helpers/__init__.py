from random import shuffle


def get_test_list(max_items=6000):
    """
    regresa una lista numérica de prueba de 0 a max_items

    """
    mi_lista = [n for n in range(max_items)]
    shuffle(mi_lista)

    return mi_lista
