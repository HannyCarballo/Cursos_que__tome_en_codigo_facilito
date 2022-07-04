# Atributos de clase. Le pertenecen a una clase, para usarlos obligatoriamente hay que usar dicha clase
# Atributos de instancia. Atributos que le pertenecen a un objeto, para usarlos hay que trabajar con el objeto

class Usuario:
    # atributos de clase
    username = 'Username por default'
    email = ''

#__dict__
user1 = Usuario()
# 1) Verifica si el atributo existe dentro del objeto
# 2) Verifica si el atributo se encuentra dentro de la clase -> lectura
# 3) Lanzar un error
print(id(user1.username)) 
print(id(Usuario.username))

print(user1.__dict__) #dict