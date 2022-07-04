def pares(): #generador -> lazy iterator
    for numero in range(0,100,2):
        yield numero #se suspende de forma 
        
        print('Se reanuda la operación')

generador = pares()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))