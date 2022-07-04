# Atributos de clase. Le pertenecen a una clase, para usarlos obligatoriamente hay que usar dicha clase
# Atributos de instancia. Atributos que le pertenecen a un objeto, para usarlos hay que trabajar con el objeto

class Usuario:
    
    # object
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
user1 = Usuario('user1', 'password1')
user2 = Usuario('user2', 'password2')

print(user1.__dict__)
print(user2.__dict__)