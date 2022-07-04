lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['C', 'C++', 'Docker']
# para conocer la longitud de una lista
print(len(lista_cursos))

# añadir elementos al final de la lista
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
print(lista_cursos)
# para conocer la longitud de una lista
print(len(lista_cursos))

# añadir elemento en cualquier posición
lista_cursos.insert(1, 'Rails')
print(lista_cursos)

# extender una lista
lista_cursos.extend(lista_cursos_2)
print(lista_cursos)
print(lista_cursos_2)

# eliminar elementos de la lista
print(lista_cursos)
lista_cursos.remove('MongoDB')
print(lista_cursos)

# eliminar elementos de la lista conociendo sus indices 
print(lista_cursos)
del lista_cursos[0]
print(lista_cursos)

# eliminar todos los elementos de la lista
lista_cursos.clear()
print(len(lista_cursos))