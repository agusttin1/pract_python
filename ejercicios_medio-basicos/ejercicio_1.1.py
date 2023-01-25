#lambda ---> funcion anonima
#sintaxis_lambda = lambda parametros : expresion a ejecutar

arr_number=[23,41,55,32,22,10,5,6,8]


#funcion filter devuelve true
#sintaxis_filter ---> filter(una_funcion(normal o anonima), una_lista(o array))

arr_par = list(filter(lambda x: x %2 == 0,arr_number))

print(arr_par)



arr_str = ["auto","moto","lancha","patineta","avion"]

arr_vocal = list(filter(lambda x : x.startswith('a'),arr_str))

print(arr_vocal)
