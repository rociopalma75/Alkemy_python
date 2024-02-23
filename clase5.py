#==================POLIMORFISMO====================
#Cualidad que tienen los objetos de tomar diferentes formas

class Auto:
    def acelerar(self):
        print("Me transporto en 4 ruedas")

class Moto:
    def acelerar(self):
        print("Me transporto en 2 ruedas")

class Camion:
    def acelerar(self):
        print("Me transporto en 18 ruedas")

#Es como que con esta funcion definida llama al metodo de la clase correspondiente
def vehiculoAcelera(vehiculo):
    vehiculo.acelerar()

# auto = Auto()
# auto.acelerar()

# moto = Moto()
# moto.acelerar()

# camion = Camion()
# camion.acelerar()
    
miVehiculo = Auto()
vehiculoAcelera(miVehiculo)

#==================ENCAPSULAMIENTO====================

class Algo:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre #Atributo privado -> get y set
        self.apellido = apellido #Atributo publico

#==================HERENCIA====================

#Clase PADRE
class Producto:
    def __init__(self, id, titulo, autor, precio, stock):
        self.id=id
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock
    
    def mostrarProducto(self): #metodo el mismo para los 3 hijos
        pass #Delega el body del metodo a los hijos

#Clases hijas
class Libro(Producto):
    def __init__(
            self, 
            id, 
            titulo, 
            autor, 
            precio, 
            stock, 
            editorial, 
            generoLiterario
        ):
        super().__init__(id,titulo,autor,precio,stock)
        self.editorial = editorial
        self.generoLiterario = generoLiterario
    
    def mostrarProducto(self):
        print(f'ID: {self.id}')
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Editorial: {self.editorial}')
        print(f'Genero Literario: {self.generoLiterario}')

class Pelicula(Producto):
    def __init__(
            self, 
            id, 
            titulo, 
            autor, 
            precio, 
            stock, 
            clasificacion, 
            generoCine
        ):
        super().__init__(id,titulo,autor,precio,stock)
        self.clasificacion = clasificacion
        self.generoCine = generoCine
    
    def mostrarProducto(self):
        print(f'ID: {self.id}')
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Clasificacion: {self.clasificacion}')
        print(f'Genero Cine: {self.generoCine}')



class Musica(Producto):
    def __init__(
            self, 
            id, 
            titulo, 
            autor, 
            precio, 
            stock, 
            formato, 
            generoMusica
        ):
        super().__init__(id,titulo,autor,precio,stock)
        self.formato = formato
        self.generoMusica = generoMusica
    
    def mostrarProducto(self):
        print(f'ID: {self.id}')
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Stock: {self.stock}')
        print(f'Formato: {self.formato}')
        print(f'Genero Musica: {self.generoMusica}')    

#ENUM
from enum import Enum

#Gnero cine
#Genero musica
#Genero libros
#Clasificacion cine
#Formato musica

class GeneroCine(Enum):
    ACCION = "Accion"
    TERROR = "Terror"
    DOCU = "Documental"

class GeneroMusica(Enum):
    RNR = "Rock"
    POP = "Pop"
    CLASICA = "Clasica"              

class GeneroLibros(Enum):
    NOVELA = "Novela"
    BIBLIOGRAFIA = "Bibliografia"
    ENSAYO = "Ensayo"

class ClasificacionCine(Enum):
    ATP = "Apto Todo Publico"
    MAS13 = "+13"
    MAS16 = "+16"
    MAS18 = "+18"

class FormatoMusica(Enum):
    CD = "Compact Disc"
    VINILO = "Disco de vinilo"
    CASSETTE = "Cassette"
  
#Para acceder a un valor del ENUM 
    #ClaseEnum.valor.value
miLibro = Libro(1,"1984", "John Green", 13000, 100, "SA", GeneroLibros.ENSAYO.value) 
miLibro.mostrarProducto()
