colores = {
    'rojo': '#FF0000',
    'verde': '#00FF00',
    'azul': '#0000FF',
    'blanco': '#FFFFFF',
    'negro': '#000000',
}

color_seleccionado = 'amarillo'

print(f'El RGB del color {color_seleccionado} es {colores.get(color_seleccionado, "No definido.")}')
