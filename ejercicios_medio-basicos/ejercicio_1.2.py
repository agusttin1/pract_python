# practica con funciones

# a) mini-quizz

yes_or_no = input('Desea realizar la siguiente quiz? (si/no): ')

def quiz(answer):
    if answer.lower() == "si":
        
        name=input("primero ingrese su nombre: ")
        print('------------------------------------------------')
        print(f'------------Bienvenido/a {name}------------')
        
        score = 0
       
        question_1 = int(input("a) cuantos jugadores se encuentran en una cancha de futbol: "))
        question_2= int(input("b) cuantos cambios se pueden hacer por partidos actualmente: "))
        if question_1 == 11:
            score = score + 1
            print('a) Respuesta acertada')
           
        else:
            print('a) respuesta incorrecta')
            
        if question_2 == 5:
            score = score + 1
            print('b) Respuesta acertada ')
            
        else:
            print('b) respuesta incorrecta')
    
        print(f'su score total fue de  {score}')
    else:
        print(f'lo esperaremos en la proxima')
        quit()
    
    
quiz(yes_or_no)


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
