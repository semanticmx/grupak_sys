
import time

from random import shuffle

from utils.ordenamientos import burbuja, heapsort, insercion, quicksort, shell

ordenamientos_validos = {
    'b': 'burbuja',
    'h': 'heapsort',
    'i': 'insercion',
    'q': 'Quick Sort',
    's': 'Shell',
}

MAX_ITEMS = 20000


class Timer:
    start_process = None
    stop_process = None

    def __init__(self):
        super().__init__()

        self.start_process = time.time() if not self.start_process else self.start_process
        print(f'Iniciando proceso en: {self.start_process}')

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
    _map_ordenamientos = {
        'b': burbuja.ordenamiento_burbuja,
        'h': heapsort.heapsort,
        'i': insercion.ordenamiento_insercion,
        'q': quicksort.quick_sort,
        's': shell.ordenamiento_shell,
    }

    def __init__(self, *args, **kwargs):
        super().__init__()

        self._tipo = kwargs.get('tipo', 'b')
        print(f'Inicializando Ordenador con {self._tipo}.')

        try:
            self._funcion = self._map_ordenamientos[self._tipo]
        except KeyError:
            print(f'Tipo de ordenamiento invalido.')

    def __str__(self):
        return f'{self.__class__.__name__}::ordenando por {self._tipo}'

    def ordenar(self):
        """
        inicia el ordenamiento

        """
        if self._funcion:
            lista = [n for n in range(MAX_ITEMS)]
            shuffle(lista)
            print(f'Ordenando...')
            self._funcion(lista)
            self.stop_timer()
        else:
            print(f'Sin algoritmo de ordenamiento.')
        print(f'Listo!...')
        self.report_performance()


if __name__ == '__main__':
    default = Ordenador()
    default.ordenar()

    heap_sort = Ordenador(tipo='h')
    heap_sort.ordenar()

    insersion = Ordenador(tipo='i')
    insersion.ordenar()

    quick = Ordenador(tipo='q')
    quick.ordenar()

    shell = Ordenador(tipo='s')
    shell.ordenar()
