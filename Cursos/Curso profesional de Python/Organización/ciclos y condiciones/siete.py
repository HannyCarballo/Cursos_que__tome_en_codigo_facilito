contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1

# Ejemplo 2 ciclo while
numero = 1234
contador_digitos = 0
while numero >= 1:
    #contador_digitos = contador_digitos + 1 # es lo mismo que la línea de abajo
    contador_digitos += 1
    numero = numero / 10 # se le quita un digito
else:
    print('Fin del ciclo while')
print(contador_digitos)