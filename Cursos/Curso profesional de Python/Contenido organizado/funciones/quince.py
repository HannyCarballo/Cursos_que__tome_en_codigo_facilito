'''
a -> la función principal(decorador)
b -> la función a decorar
c -> la función decorada
'''
def a(b):

    def c(*args, **kwargs):
        print('Antes del llamado')
        resultado = b(*args, **kwargs)
        print('Después del llamado')
        return resultado
    return c

'''
@a
def saludar():
    print('Hola, nos encontramos en una función')
saludar()
'''

@a
def suma(n1, n2):
    return n1 + n2
resultado = suma(10,20)
print(resultado)