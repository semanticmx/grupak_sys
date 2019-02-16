
import time

from random import shuffle

from utils.ordenamientos import burbuja, heapsort, insercion, quicksort, shell

MAX_ITEMS = 450000


class Timer:
    start_process = None
    stop_process = None

    def __init__(self):
        super().__init__()

        self.start_process = time.time() if not self.start_process else self.start_process

    def stop_timer(self):
        self.stop_process = time.time()

    def report_performance(self):
        print(f'Tomó: {self.stop_process - self.start_process} tiempo.')


class Ordenador(Timer):
    """
    ordena una lista por varios métodos

    """
    _tipo = 'burbuja'
    _funcion = None
    _lista = []
    _max_items = MAX_ITEMS

    _map_ordenamientos = {
        'b': burbuja.ordenamiento_burbuja,
        'h': heapsort.heapsort,
        'i': insercion.ordenamiento_insercion,
        'q': quicksort.quick_sort,
        's': shell.ordenamiento_shell,
    }

    ordenamientos_validos = {
        'b': 'Burbuja',
        'h': 'Heap Sort',
        'i': 'Insercion',
        'q': 'Quick Sort',
        's': 'Shell',
    }
    def __init__(self, *args, **kwargs):
        super().__init__()

        self._tipo = kwargs.get('tipo', 'b')
        self._lista = kwargs.get('lista')  # regresa un None si no está definida lista
        self._max_items = kwargs.get('max_items', MAX_ITEMS)

        try:
            self._funcion = self._map_ordenamientos[self._tipo]
        except KeyError:
            print(f'Tipo de ordenamiento invalido.')

        print(f'Inicializando Ordenador con {self.ordenamientos_validos[self._tipo]}.')

    def __str__(self):
        return f'{self.__class__.__name__}::ordenando por {self._tipo}'

    def __getattribute__(self, item):
        """
        regresa el valor de item

        """
        if item != '_lista':
            return super().__getattribute__(item)

        valor = super().__getattribute__(item)

        if not valor:
            lista = [n for n in range(self._max_items)]
            shuffle(lista)
            return lista

        return valor

    def iniciar(self):
        """
        inicia el ordenamiento

        """
        if self._funcion:
            print(f'Ordenando {self._max_items} elementos')
            lista = self._funcion(self._lista)
            self.stop_timer()
        else:
            print(f'Sin algoritmo de ordenamiento.')
        print(f'Listo. de {lista[0]} a {lista[-1]}')
        self.report_performance()


if __name__ == '__main__':
    default = Ordenador(max_items=6000)
    default.iniciar()

    heap_sort = Ordenador(tipo='h', max_items=95000)
    heap_sort.iniciar()

    insersion = Ordenador(tipo='i', max_items=10000)
    insersion.iniciar()

    quick = Ordenador(tipo='q', max_items=500000)
    quick.iniciar()

    shell = Ordenador(tipo='s', max_items=250000)
    shell.iniciar()
