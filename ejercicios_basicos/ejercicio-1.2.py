frase = input('ingresa una frase y calculo cuanto tardarias si tuvieras que decirla: ')

palabras_separadas = frase.split(" ")

cantidad_palabras = len(palabras_separadas)


if cantidad_palabras > 120:
    print('mucho texto')
    
    
print(f'Dijiste {cantidad_palabras} palabras y tardarias en decirlas {cantidad_palabras / 2} segundos en decirlo ')



