#lambda ---> funcion anonima
#sintaxis_lambda = lambda parametros : expresion a ejecutar

arr_number=[23,41,55,32,22,10,5,6,8]


#funcion filter devuelve true
#sintaxis_filter ---> filter(una_funcion(normal o anonima), una_lista(o array))

arr_par = list(filter(lambda x: x%2 == 0,arr_number))

#print(arr_par)



arr_str = ["auto","moto","lancha","patineta","avion"]
arr_vocal = list(filter(lambda x : x.startswith('a'),arr_str))

#print(arr_vocal)


#funcion map a diferencia del filter itera todos los elementos de una lista, por ende pueden ser cambiados sus valores


arr_number_map = [2,6,12,20]

arr_expo = list(map(lambda x : x**2 , arr_number_map))

#print(arr_expo)


enteros = [1, 2, 4, 7]
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3
funciones = [cuadrado, cubo]


for e in enteros:
    valores = list(map(lambda x : x(e), funciones))




verbos = ['correr','caminar','programar','entrenar','comer','saltar']

tiempo =[2,4,5,2,1,3]


def sentencia_uno(verbo1,tiempo1):
    return f"hoy me toco {verbo1} durante {tiempo1} horas "

funcion = [sentencia_uno]

for e,u in zip(verbos,tiempo):
    sentencias =list(map(lambda x: x(e,u) , funcion))
    print(sentencias)




