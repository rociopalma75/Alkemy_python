from enum import Enum

class TipoInstrumento(Enum):
    CAT1 = "Viento"
    CAT2 = "Cuerdas"
    CAT3 = "Percusion"

class Fabrica:
    def __init__(self):
        self.sucursales = []

    def agregarSucursal(self, sucursal):
        self.sucursales.append(sucursal)

    def listarInstrumentos(self):
        for sucursal in self.sucursales:
            print(f'SUCURSAL: {sucursal.nombre}')
            for instrumento in sucursal.instrumentos:
                mostrarInstrumento(instrumento)
            
    def instrumentosPorTipo(self, tipoInstrumento):
        for sucursal in self.sucursales:
            print(f'SUCURSAL: {sucursal.nombre}')
            for instrumento in sucursal.instrumentos:
                if instrumento.tipo == tipoInstrumento:
                    mostrarInstrumento(instrumento)

    def borrarInstrumento(self, idInstrumento):
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.id == idInstrumento:
                    sucursal.instrumentos.remove(instrumento)

    def porcPorTiposInstrumento(self, nombreSucursal):
        for sucursal in self.sucursales:
            if sucursal.nombre == nombreSucursal:
                calcularPorcInstrumentos(sucursal.instrumentos)

def mostrarInstrumento(instrumento):
    print(f'Id: {instrumento.id}')
    print(f'Precio: {instrumento.precio}')
    print(f'Tipo: {instrumento.tipo}')
    print(".........")

def calcularPorcInstrumentos(instrumentosSucursal):
    cantidadInstrumentos = len(instrumentosSucursal)
    contadorViento = 0
    contadorCuerda = 0
    contadorPercusion = 0

    for instrumento in instrumentosSucursal:
        if instrumento.tipo == TipoInstrumento.CAT1.value:
            contadorViento += 1
        elif instrumento.tipo == TipoInstrumento.CAT2.value:
            contadorCuerda += 1
        else:
            contadorPercusion+= 1
    
    print(f'Porcentaje: Viento: {(contadorViento/cantidadInstrumentos)*100}')
    print(f'Porcentaje: Cuerda: {(contadorCuerda/cantidadInstrumentos)*100}')
    print(f'Porcentaje: Percusion: {(contadorPercusion/cantidadInstrumentos)*100}')

class Sucursal():
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumentos(self, instrumento):
        self.instrumentos.append(instrumento)

class Instrumento():
    def __init__(self, id, precio, tipo):
        self.id = id
        self.precio = precio
        self.tipo = tipo

i1 = Instrumento("122AA", 12000,TipoInstrumento.CAT1.value)
i2 = Instrumento("120AA", 45000, TipoInstrumento.CAT2.value)
i3 = Instrumento("121AA", 45200, TipoInstrumento.CAT3.value)
i4 = Instrumento("125AA", 45400, TipoInstrumento.CAT1.value)

s1 = Sucursal("Sucursal 1")
s2 = Sucursal("Sucursal 2")

s1.agregarInstrumentos(i1)
s1.agregarInstrumentos(i2)
s2.agregarInstrumentos(i3)
s2.agregarInstrumentos(i4)

f = Fabrica()
f.agregarSucursal(s1)
f.agregarSucursal(s2)

f.borrarInstrumento("125AA")

f.listarInstrumentos()

f.porcPorTiposInstrumento("Sucursal 1")
