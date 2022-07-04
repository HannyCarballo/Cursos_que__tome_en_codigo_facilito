# * para poner n cantidad de parámetros, es una tupla
# def promedio(*args): # *args es una convención de la comunidad Python
def promedio(*listado):
    print(listado)
    print(type(listado))
    return sum(listado) / len(listado)

resultado = promedio(10,10,5,7,10)
print(resultado)


def combinacion(p1,p2,*args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)
combinacion(10,20,1,2,3,4,5,6,7,8, p4=1000)

# hay dos saltos entre cada función