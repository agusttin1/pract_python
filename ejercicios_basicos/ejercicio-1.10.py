#area de una esfera
# AREA = 4 * PI * RADIO**2

#volumen de una esfera
#VOLUMEN = 1/3 * PI * RADIO**3

import math

radio_esfera = float(input('ingrese el radio de una esfera: '))


area_esfera = 4 * math.pi * pow(radio_esfera,2)

v_esfera = 1/3 * math.pi * pow(radio_esfera,3) 


print(f'el area de la esfera es de {round(area_esfera,2)}')

print(f'el volumen de la esfera es de {round(v_esfera,2)}')
