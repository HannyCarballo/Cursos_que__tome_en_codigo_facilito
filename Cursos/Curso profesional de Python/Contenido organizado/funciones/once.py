promedio = lambda *args : sum(args)/len(args)
print(promedio(10,10,9,8,7))

aprobatorio = lambda calificacion : calificacion >= 7
print(aprobatorio(5))


def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}.')
    else:
        print('No aprobaste la materia.')
mostrar_mensaje(promedio, aprobatorio, 10,10,8,7,7)