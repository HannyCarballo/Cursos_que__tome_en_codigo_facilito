elementos  = {}

elementos['nombre'] = 'Cody' # crea la llave con su valor
print(elementos)
print(len(elementos))

elementos[(1,2,3)] = 'La llave es una tupla'
print(elementos)
print(len(elementos))

elementos['nombre'] = 'Códigofacilito' # se actualiza el valor de la llave
print(elementos)
print(len(elementos))

elementos = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
print(elementos)
print(len(elementos))