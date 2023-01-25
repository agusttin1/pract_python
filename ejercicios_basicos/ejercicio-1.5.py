import math


radio_circuferencia = float(input('ingrese el radio de un circulo: '))


formula_area =  math.pi * pow(radio_circuferencia,2)
formula_longitud= 2 * math.pi * radio_circuferencia

print('------------------------')

print(f'el area de la circuferencia segun su radio es de {round(formula_area,2)}')

print('------------------------')

print(f' la longitud de la circuferencia segun su radio es de {round(formula_longitud,2)}')
