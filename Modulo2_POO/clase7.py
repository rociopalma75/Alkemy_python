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
                instrumento.mostrarInstrumento()
            
    def instrumentosPorTipo(self, tipoInstrumento):
        for sucursal in self.sucursales:
            print(f'SUCURSAL: {sucursal.nombre}')
            for instrumento in sucursal.instrumentos:
                if instrumento.tipo == tipoInstrumento:
                    instrumento.mostrarInstrumento()

    def borrarInstrumento(self, idInstrumento):
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.id == idInstrumento:
                    sucursal.instrumentos.remove(instrumento)

    def porcPorTiposInstrumento(self, nombreSucursal):
        for sucursal in self.sucursales:
            if sucursal.nombre == nombreSucursal:
                sucursal.calcularPorcInstrumentos()
                break

class Sucursal():
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumentos(self, instrumento):
        self.instrumentos.append(instrumento)
    
    def calcularPorcInstrumentos(self):
        cantidadInstrumentos = len(self.instrumentos)
        contadorViento = 0
        contadorCuerda = 0
        contadorPercusion = 0
        
        for instrumento in self.instrumentos:
            if instrumento.tipo == TipoInstrumento.CAT1.value:
                contadorViento += 1
            elif instrumento.tipo == TipoInstrumento.CAT2.value:
                contadorCuerda += 1
            else:
                contadorPercusion += 1
        
        porc = lambda a : (a/cantidadInstrumentos)*100

        print(f'Porcentaje de Viento: %{porc(contadorViento)}')
        print(f'Porcentaje de Cuerda: %{porc(contadorCuerda)}')
        print(f'Porcentaje de Percusion: %{porc(contadorPercusion)}')

class Instrumento():
    def __init__(self, id, precio, tipo):
        self.id = id
        self.precio = precio
        self.tipo = tipo
    
    def mostrarInstrumento(self):
        print(f'ID: {self.id} - Precio: ${self.precio} - Tipo: {self.tipo}')

i1 = Instrumento("122AA", 12000,TipoInstrumento.CAT1.value)
i2 = Instrumento("120AA", 45000, TipoInstrumento.CAT2.value)
i3 = Instrumento("121AA", 45200, TipoInstrumento.CAT3.value)
i4 = Instrumento("125AA", 45400, TipoInstrumento.CAT1.value)
i5 = Instrumento("125AB", 25400, TipoInstrumento.CAT2.value)
i6 = Instrumento("125AC", 35400, TipoInstrumento.CAT2.value)
i7 = Instrumento("125AD", 15400, TipoInstrumento.CAT3.value)

s1 = Sucursal("Sucursal 1")
s2 = Sucursal("Sucursal 2")

s1.agregarInstrumentos(i1)
s1.agregarInstrumentos(i2)
s1.agregarInstrumentos(i5)
s1.agregarInstrumentos(i6)
s1.agregarInstrumentos(i7)
s2.agregarInstrumentos(i3)
s2.agregarInstrumentos(i4)

f = Fabrica()
f.agregarSucursal(s1)
f.agregarSucursal(s2)


#Punto A
print("LISTADO DE TODOS LOS INSTRUMENTOS")
f.listarInstrumentos()
print("========================")

#Punto B
print("INSTRUMENTOS POR TIPO")
f.instrumentosPorTipo(TipoInstrumento.CAT3.value)
print("========================")

#Punto C
print("Se borra el instrumento id: 125AA")
f.borrarInstrumento("125AA")
print("========================")
f.listarInstrumentos()
print("========================")

#Punto D
print("PORCENTAJE POR TIPOS")
f.porcPorTiposInstrumento("Sucursal 1")
