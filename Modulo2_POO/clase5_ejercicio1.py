class Bicicleta:
    def __init__(self,marca, modelo, color, rodado, precio, cambios, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.rodado = rodado
        self.precio = precio
        self.cambios = cambios
        self.velocidad = velocidad
    
    def mostrarBici(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Color: {self.color}')
        print(f'Rodado: {self.rodado}')
        print(f'Precio: {self.precio}')
        print(f'Cambios: {self.cambios}')
        print(f'Velocidad: {self.velocidad}')

    def actualizarPrecio(self, porcentaje):
        print("Precio anterior: ", self.precio)
        self.precio += self.precio * (porcentaje/100)
        print("Precio actual: ", self.precio)

    def frenar(self):
        while(self.velocidad>=0):
            self.velocidad -= 1
            print("Velocidad actual: ", self.velocidad)
        print("ya frenaste")

        

miBici = Bicicleta("Venzo", "XR", "Rojo", 29,19,3000,15)
miBici.mostrarBici()
print("===================================")
miBici.actualizarPrecio(20)
print("===================================")
miBici.frenar()