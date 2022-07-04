diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(len(diccionario))

# eliminando elemento. método 1) del
del diccionario['a']
print(diccionario)
print(len(diccionario))

# eliminando elemento. método 2) pop
# si se pone un elemento que no existe, manda error
valor = diccionario.pop('b')
print(valor)
print(diccionario)
print(len(diccionario))

# eliminando todos los elementos. método 3) clear
diccionario.clear()
print(diccionario)
print(len(diccionario))
