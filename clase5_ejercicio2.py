from enum import Enum

class Tipo(Enum):
    V = "Vertebrado"
    I = "Invertebrado"

class Animal:
    def __init__(self,cantidad_patas,tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo
    
    def comer(self):
        return "Estoy comiendo"
    
    def mostrar(self):
        pass
    
    
class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza
    
    def correr(self):
        return "Estoy corriendo"
    
    def mostrar(self):
        print(f'Cantidad de patas: {self.cantidad_patas}')
        print(f'Tipo: {self.tipo}')
        print(f'Nombre: {self.nombre}')
        print(f'Raza: {self.raza}')


class Aguila(Animal):
    def __init__(self,cantidad_patas,tipo):
        super().__init__(cantidad_patas,tipo)

    def volar(self):
        return "Estoy volando"
    
    def mostrar(self):
        print(f'Cantidad de patas: {self.cantidad_patas}')
        print(f'Tipo: {self.tipo}')

perro1 = Perro(4,Tipo.V.value, "Coqui","Labrador")
print(perro1.correr())
perro1.mostrar()

print("===========================")

aguila1 = Aguila(2, Tipo.V.value)
print(aguila1.volar())
aguila1.mostrar()
