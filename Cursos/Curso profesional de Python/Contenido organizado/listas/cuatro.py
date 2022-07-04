lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
# [start:end]
sub_lista = lista_cursos[0:3]
print(sub_lista)

sub_lista = lista_cursos[1:4]
print(sub_lista)

# no manda error
sub_lista = lista_cursos[1:100]
print(sub_lista)

# aquí se indica que se quiere los últimos elementos de la lista a partir del inicial
# [start:]
sub_lista = lista_cursos[1:]
print(sub_lista)

# aquí se indica que se quiere los primeros elementos de la lista
# [:end]
sub_lista = lista_cursos[:4]
print(sub_lista)

# generando saltos en la lista
# [start:end:skip]
sub_lista = lista_cursos[1:5:2]
print(sub_lista)

# sublista con todos los elementos de la lista original
sub_lista = lista_cursos[:]
print(sub_lista)

# elementos de la lista con saltos de dos en dos
sub_lista = lista_cursos[::2]
print(sub_lista)

# lista inversa
sub_lista = lista_cursos[::-1]
print(sub_lista)