
# R G B
# Red Green Blue
# 0 -> 256
# 00 -> FF

colores = {
    'rojo': '#FF0000',
    'verde': '#00FF00',
    'azul': '#0000FF',
    'blanco': '#FFFFFF',
    'negro': '#000000',
}

color_seleccionado = 'amarillo'

print(f'El RGB del color {color_seleccionado} es {colores.get(color_seleccionado, "No definido.")}')

# # print(f'El código RGB del color {color} es : {colores[color]}')
#
#
# def get_rgb(color):
#     """
#     regresa el valor RGB de color
#
#     >>> get_rgb('azul')
#     El RGB del color azul es #0000FF
#
#     """
#     try:
#         print(f'El RGB del color {color} es {colores[color]}')
#     except KeyError:
#         print(f'El color {color} no está definido.')
#
#
# get_rgb(color=color_seleccionado)

# List

# letras = ['H', 'o', 'l', 'a']
#
# print(letras.pop().upper())
#
# print(letras)
#
# print(letras.pop())
# print(letras)
# print(letras.pop())
# print(letras.pop())
# print(letras)
#
#
# # Tipos de dato entero
#
# uno = 345
#
# dos = 543
#
# print(uno + dos)
# print(uno - dos)
# print(uno * dos)
# print(uno / dos)
#
# # Tipos de dato flotante
#
# uno = 1.3
# dos = 0.0
#
# print(uno + dos)
# print(uno - dos)
# print(uno * dos)
#
#
# try:
#     print(uno / dos)
# except ZeroDivisionError:
#     # f-strings
#     print(f'División entre cero: {uno} / {dos}')
#
