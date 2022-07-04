rango = range(11) # va del 0 al 10
print(rango)

for valor in rango:
    print(valor)

for valor in range(21):
    print(valor)

for valor in range(5, 11):
    print(valor)

for valor in range(5, 11, 2):
    print(valor)

# range(start, end, skips)

numeros = [10,20,30,40,50]
#                              iterando, valor indice inicial
for indice, numero in enumerate(numeros, 10):
    print(indice, numero)