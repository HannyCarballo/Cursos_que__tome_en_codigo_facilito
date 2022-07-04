# scope. el alcance de las variables 
# animal de la línea 2 y de la línea 5 son distintos
animal = 'Leon' #VariableGlobal

def imprimir_animal():
    global animal 
    animal = 'ballena'
    print(animal) #VariableGlobal
    #print(animal) #VariableLocal
imprimir_animal()
print(animal)
