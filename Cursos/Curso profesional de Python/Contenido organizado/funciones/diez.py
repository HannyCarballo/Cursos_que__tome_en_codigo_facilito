# funciones lambda
# usa una sola línea de código y no posee un nombre
# realiza tareas muy pequeñas

funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(10))

'''
sin parametros = lambda True
parametros default = lambda p1=10, p2=20, p3=30 : p1+p2+p3

asterisco = lambda *args, **kwargs : len(args) +len(kwargs)
'''