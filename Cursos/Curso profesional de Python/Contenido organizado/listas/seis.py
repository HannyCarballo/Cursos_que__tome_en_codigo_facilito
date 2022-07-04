lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
# ordenando lista de mayor a menor
lista.sort(reverse = True)
print(lista)

# ordenando lista de menor a mayor
lista.sort()
print(lista)

print(lista[0]) #min
print(lista[-1]) #max

print(min(lista))
print(max(lista))

# Saber si un elemento se encuentra en la lista
print(10 in lista)
print(5 in lista)
print(11 not in lista)