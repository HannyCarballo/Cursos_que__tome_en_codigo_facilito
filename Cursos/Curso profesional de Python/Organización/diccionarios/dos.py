diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print('d' in diccionario)
valor = diccionario['d']
print(valor)
'''
valor = diccionario['z']
print(valor)
esto manda error 
'''

# Método get
valor = diccionario.get('d')
print(valor)
valor = diccionario.get('z') # no manda error
print(valor)
valor = diccionario.get('z', 'La llave no existe en el diccionario') # puede recibir otro parámetro
print(valor)

# Método setdefault. es la contraparte del método get
valor = diccionario.setdefault('e', 5)
print(valor)

print(diccionario)