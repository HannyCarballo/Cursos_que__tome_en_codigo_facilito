def pares(): #generador -> lazy iterator
    for numero in range(0,100,2):
        yield numero #se suspende de forma 
        
        print('Se reanuda la operación')

for par in pares():
    pares()