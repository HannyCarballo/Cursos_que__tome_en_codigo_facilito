'''
Nos permiten comparar tipos booleanos
and, or y not
'''
resultado_final = True and True
print(resultado_final)

resultado_final = True and True and 10 > 20
print(resultado_final)

resultado_final = False or False and 100 > 20
print(resultado_final)

resultado_final = True and (False or 50 > 10)
print(resultado_final)

resultado_final = not True 
print(resultado_final)