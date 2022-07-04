cursos = ['Python', 'Django', 'Flask']

niveles = ('Básico', 'Intermedio', 'Avanzado')

# generando una tupla a partir de una lista
cursos_tupla=tuple(cursos)
print(cursos_tupla)
print(type(cursos_tupla))

# generando una lista a partir de una tupla
niveles_lista = list(niveles)
print(niveles_lista)
print(type(niveles_lista))