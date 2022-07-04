def radio_circulo(radio, pi=3.14): #los valores por default siempre van a la derecha
    return pi * (radio ** 2)

resultado = radio_circulo(10, 3.141592)
print(resultado)

resultado = radio_circulo( pi=3.141592,radio=10)
print(resultado)