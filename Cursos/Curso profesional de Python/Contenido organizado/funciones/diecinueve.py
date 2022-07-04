# docstring
# __doc__ (Módulos, clases, métodos y funciones)
# para testear funciones: python -m doctest diecinueve.py
def suma(n1,n2):
    """
    La función suma dos números enteros
    Argumentos: n1 y n2 de tipo entero
    Se retorna la suma de los parámetros

    >>> suma(10,20)
    30

    >>> suma(100,200)
    300

    """
    return n1 + n2 
#print(suma.__doc__)
print(help(suma))
