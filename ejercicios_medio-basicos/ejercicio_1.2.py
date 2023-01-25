# practica con funciones

# a) mini-quizz




#b)

diccionario = {
    'river plate': "4 libertadores",
    'boca juniors': "6 libertadores",
    'independiente':"7 libertadores",
    'san lorenzo': "1 libertadores"
}


for i in diccionario.items():
        key= i[0]
        value = i[1]
        print(f'el equipo {key}, tiene una cantidad de {value}')
    

#c)

def filter_sueldo(cant_sueldo):
    
    lista_sueldo = list()
    
    for i in range(cant_sueldo):
        sueldo = float(input("ingrese los sueldos: "))
        lista_sueldo.append(sueldo)
    sueldo_max = max(lista_sueldo)
    sueldo_min = min(lista_sueldo)
    return sueldo_max,sueldo_min


sueldo_max,sueldo_min = filter_sueldo(5)

print(f'el sueldo minimo es de :{sueldo_min} y el maximo es de: {sueldo_max}')
