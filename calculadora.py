"""
Implementa una calculadora que suma, resta, multiplica,
divide y obtiene el residuo entero de una división

"""


def suma(x, y):
    """
    suma x + y

    """
    return x + y


def resta(x, y):
    """
    resta x - y

    """
    return x - y


def multiplicacion(x, y):
    """
    multiplica x * y

    """
    return x * y


def division(x, y):
    """
    divide x / y, y valida división entre 0

    """
    try:
        return x / y
    except ZeroDivisionError:
        return 'ERR'


def modulo(x, y):
    """
    regresa el residuo entero de la división de x / y

    """
    return x % y


operaciones = {
    '+': suma,
    '-': resta,
    '*': multiplicacion,
    '/': division,
    'res': modulo,
}


def calculadora(operacion, operando_1, operando_2):
    """
    ejecuta operacion entre operando_1 y operando_2 y regresa el resultado

    >>> calculadora('+', 4, 8)
    12
    >>> calculadora('*', 3, 2)
    6
    >>> calculadora('-', 5, 10)
    -5
    >>> calculadora('/', 20, 5)
    4.0
    >>> calculadora('res', 10, 3)
    1
    >>> calculadora('/', 10, 0)
    ERR

    """
    return print(operaciones[operacion](x=operando_1, y=operando_2))


calculadora('+', 4, 8)
calculadora('*', 3, 2)
calculadora('-', 5, 10)
calculadora('/', 20, 5)
calculadora('res', 10, 3)
calculadora('/', 10, 0)
