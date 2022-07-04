def funcion_principal():
    a = 'a' 
    b = 'b' # variables locales

    def funcion_anidada():
        c = 'c' # variables locales

        nonlocal b
        b = 'Cambio de valor'

        print(a)
        print(b)
    
    funcion_anidada()
funcion_principal()