# un * será una tupla
def promedio(*args):
    return sum(args) / len(args)


# doble * será un diccionario
def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))
usuarios(eduardo = [10,10,8], fernando = [10,9,9])

def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)
combinacion(1,2,3,4,5, cody = True, curso = 'Python')