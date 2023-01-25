#datos: radio del cono(real), altura del cono (real), generatriz del cono(real)


#area de la base del cono 
# Area Base =math.pi * pow(radio,2)


#area lateral del cono
# Area Lateral = math.pi * radio * generatriz

#area total
#Area Total = AB + AL

#volumen del cono
#V = (1/3) * AB * ALTURA



import math


radio = float(input('ingrese el radio del cono: '))
print('--------------')
altura = float(input('ingrese la altura del cono: '))
print('--------------')
generatriz = float(input('ingrese la generatriz del cono: '))
print('--------------')


area_base = math.pi * pow(radio,2)

area_lateral = math.pi * radio * generatriz

area_total = area_base + area_lateral

volumen_total = (1/3) * area_base * altura



print('--------------')
print(f"El area base del cono es de , {round(area_base,2)}")
print('--------------')
print(f"El area total del cono es de , {round(area_total,2)}")
print('--------------')
print(f"El area lateral del cono es de , {round(area_lateral,2)}")
print('--------------')
print(f"El volumen total del cono es de , {round(volumen_total,2)}")
print('--------------')
