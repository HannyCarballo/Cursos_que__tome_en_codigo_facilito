# Buscando strings dentro de otros strings
titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'

# 1) Método count. Nos permite contar cuantas veces existe un string dentro de otro
contador = titulo_curso.count('Python')
print(contador)
contador = titulo_curso.count('o')
print(contador)

# 2) Usando la palabra reservada in, retorna un booleano
print('python' in titulo_curso.lower())
print('codigofacilito' not in titulo_curso.lower())

# 3) startswith. ver si una palabra está al inicio. Retorna un valor booleano
print(titulo_curso.startswith('Curso'))
print(titulo_curso.startswith('Python'))

# 4) endswith. ver si una palabra se encuentra al final. Retorna un valor booleano
print(titulo_curso.endswith('Curso'))
print(titulo_curso.endswith('Python'))