variable = 'Cody' or 'Codigofacilito'
# Python asignará el primer nombre verdadero con el cual se tope
print(variable)

variable = '' or 0 or 0.0 or [] or True
print(variable)

listado = [1]
nombre = 'Cody'
if listado:
    variable = listado
else:
    variable = nombre
print(variable)

variable = listado or nombre
print(variable)