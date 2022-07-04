def suma(n1, n2):
    return n1 + n2 , 'La función retorna dos valores'
numero_uno = int(input('Ingresa el primer número entero: '))
numero_dos = int(input('Ingresa el segundo número entero: '))

resultado, _ = suma(numero_uno, numero_dos)
print('El resultado es:', resultado)