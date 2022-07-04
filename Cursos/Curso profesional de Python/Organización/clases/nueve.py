class Animal(): #clase padre
    def comer(self):
        print('El animal come.')       
    
    def dormir(self):
        print('El animal duerme.')


class Mascota(Animal): #clase padre
    def comer(self):
        print('La mascota come.')  

class Felino:

    def cazar(self):
        print('El felino caza')

class Gato(Mascota, Felino): #clase hija
    
    def __init__(self,nombre):
        self.nombre = nombre
    def comer(self):
        super().comer()
        print(f'{self.nombre} come.')
    def dormir(self):
        print(f'{self.nombre} duerme.')

patricio = Gato('Patricio')
patricio.comer()
patricio.dormir()
patricio.cazar()