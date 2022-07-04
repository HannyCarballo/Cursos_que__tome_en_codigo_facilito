# Atributos de clase. Le pertenecen a una clase, para usarlos obligatoriamente hay que usar dicha clase
# Atributos de instancia. Atributos que le pertenecen a un objeto, para usarlos hay que trabajar con el objeto

class Usuario:
    username = 'Username por default'
    email = ''

Usuario.username = 'user1'
Usuario.email = 'info@codigofacilito.com' 
print(Usuario.username)
print(Usuario.email)