# existen dos palabras que nos permitirán modificar el comportamiento de nuestros ciclos
titulo_curso = 'Curso profesional de Python'

for caracter in titulo_curso:
    print(caracter)

# break finaliza de forma inmediata
for caracter in titulo_curso:
    if caracter == 'P':
        break
    print(caracter)

# continue se salta ese carácter
for caracter in titulo_curso:
    if caracter == 'o':
        continue
    print(caracter)