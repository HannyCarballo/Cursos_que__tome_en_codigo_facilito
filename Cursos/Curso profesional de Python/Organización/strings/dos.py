# los strings son inmutables

nombre = 'Hanny'
apellido = 'Carballo Ramírez'

# concatenando. método 1
nombre_completo = nombre + ' ' + apellido + '.'
print (nombre_completo)

# concatenando. método 2
nombre_completo = 'Ms. %s %s.' %(nombre, apellido)
print(nombre_completo) 

# concatenando. método 3 placeholders
nombre_completo = 'Ms. {} {}.'.format(nombre, apellido)
print(nombre_completo)
# ----------
nombre_completo = 'Ms. {nombre} {apellido}.'.format(
nombre = nombre,
apellido = apellido
)
print(nombre_completo)

# concatenando. método 4 usando interpolación con el método fstring
nombre_completo = f'Ms. {nombre} {apellido} {6*3} {"años"}'
print(nombre_completo)