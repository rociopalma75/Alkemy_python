# POO
# 1RA PARTE -> Atributos y Propiedades
# 2DA PARTE -> Metodos
# 3RA PARTE -> Estados


class Auto:
    #================1RA PARTE==================
    #CONSTRUCTOR - Aca definimos los atributos
    def __init__(self, marca, modelo, color, estadoMotor, estadoCambios, velocidades):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.estadoMotor = estadoMotor
        self.estadoCambios = estadoCambios
        self.velocidades = velocidades

    #================2DA PARTE==================
    #Metodos 
    #Getters - metodos que nos permiten mostrar los atributos fuera del contexto de la clase
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo
    
    def getColor(self):
        return self.color
    
    def getAuto(self):
        print("Marca: ", self.getMarca())
        print("Modelo: ", self.getModelo())
        print("Color: ", self.getColor())

    #================3RA PARTE==================

    def cambiarEstadoMotor(self):
        if(self.estadoMotor):
            print("Motor prendido, lo voy a apagar")
            self.estadoMotor = False
            print("Motor apagado")
        else:
            print("Motor apagado, lo voy a encender")
            self.estadoMotor = True
            print("Motor encendido")    

    def subirVelocidad(self):
        cambioActual = self.estadoCambios
        if(self.estadoCambios < self.velocidades):
            self.estadoCambios += 1
            print(f'El {self.getModelo()} estaba en {self.estadoCambios - 1}, ahora esta en {self.estadoCambios}')
        else:
            print("Estas en el cambio mas alto")

    def bajarVelocidad(self):
        cambioActual = self.estadoCambios
        if(self.estadoCambios > -1):
            self.estadoCambios -= 1
            print(f'El {self.getModelo()} estaba en {self.estadoCambios + 1}, ahora esta en {self.estadoCambios}')
        else:
            print("Estas en el cambio mas bajo")

auto1 = Auto("Toyota", "Prius", "Blanco", True,1, 6)
# print(auto1) #Esto asi no funciona, no significa nada 
auto1.getAuto()
auto1.cambiarEstadoMotor()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()

