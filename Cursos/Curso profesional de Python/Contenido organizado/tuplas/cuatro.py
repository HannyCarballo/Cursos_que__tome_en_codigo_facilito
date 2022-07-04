# podemos declarar variables en una sola línea
uno, dos, tres, cuatro = 1, 2, 3, 4
print(uno)
print(dos)
print(tres)
print(cuatro)

# se puede hacer exactamente lo mismo con tuplas
numeros = (1, 2, 3, 4)
uno, dos, tres, cuatro = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)

# cuando no sepamos la cantidad de números que haya
numeros = (1, 2, 3, 4, 5, 6, 7, 8)
uno, dos, tres, cuatro, *resto_valores = numeros  # * -> lista
print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores) # se almacena como una lista, no se desempaqueta

# cuando no se quiera trabajar con los siguientes valores
numeros = (1, 2, 3, 4, 5, 6, 7, 8)
uno, dos, tres, cuatro, *_ = numeros  # _ -> no se quiere trabajar con los demás valores. omitir valor
print(uno)
print(dos)
print(tres)
print(cuatro)

# se excluyen algunos elementos
numeros = (1, 2, 3, 4, 5, 6, 7, 8)
uno, _, tres, _, _, seis, siete, _ = numeros  # _ -> no se quiere trabajar con los demás valores. omitir valor
print(uno)
print(tres)
print(seis)
print(siete)