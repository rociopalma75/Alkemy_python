from enum import Enum

class CatEmpleado(Enum):
    CAT1 = "Por Comision"
    CAT2 = "Salario Fijo"

class CatAntiguedad(Enum):
    CAT1 = "Menos de 2 años"
    CAT2 = "Entre 2 y 5 años"
    CAT3 = "Mas de 5 años"

class Empleado:
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContratacion):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioIngreso = anioIngreso
        self.tipoContratacion = tipoContratacion
    
    def mostrarSalario():
        pass

    def mostrarEmpleado(self):
        print(f'Nombre y Apellido: {self.apellido}, {self.nombre}')
        print(f'DNI: {self.dni}')
        print(f'Ingreso: {self.anioIngreso}')
        print(f'Categoria: {self.tipoContratacion}')
        

class PorComision(Empleado):
    def __init__(self, 
                 dni, 
                 nombre, 
                 apellido, 
                 anioIngreso, 
                 salarioMinimo, 
                 clientesCaptados, 
                 montoPorCliente):
        super().__init__(dni,nombre,apellido,anioIngreso, CatEmpleado.CAT1.value)
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente

    def mostrarSalario(self):
        salario = self.clientesCaptados * self.montoPorCliente
        if salario >= self.salarioMinimo:
            self.salarioMinimo = salario
        print(f'{self.apellido}, {self.nombre} -> {self.salarioMinimo}')

    def mostrarEmpleado(self):
        super().mostrarEmpleado()
        print(f'Salario Minimo: {self.salarioMinimo}')
        print(f'Clientes captados: {self.clientesCaptados}')
        print(f'Monto por cliente: {self.montoPorCliente}')


class SueldoFijo(Empleado):
    def __init__(self, 
                 dni, 
                 nombre, 
                 apellido, 
                 anioIngreso, 
                 sueldoBasico
                ):
        super().__init__(dni,nombre,apellido,anioIngreso, CatEmpleado.CAT2.value)
        self.sueldoBasico = sueldoBasico
        self.antiguedad = self.setAntiguedad()
        self.porcAdicional = self.setPorcAdicional()

    def setAntiguedad(self):
        antiguedadAnios = 2024 - self.anioIngreso
        if antiguedadAnios <= 2:
            return CatAntiguedad.CAT1.value
        elif antiguedadAnios > 2 and antiguedadAnios <= 5:
            return CatAntiguedad.CAT2.value
        else:
            return CatAntiguedad.CAT3.value

    def setPorcAdicional(self):
        if self.antiguedad == CatAntiguedad.CAT1.value:
            return 0
        elif self.antiguedad == CatAntiguedad.CAT2.value:
            return 0.05
        else:
            return 0.10

    def mostrarSalario(self):
        self.sueldoBasico += self.sueldoBasico * self.porcAdicional
        print(f'{self.apellido},{self.nombre} -> ${self.sueldoBasico}')

    def mostrarEmpleado(self):
        super().mostrarEmpleado()
        print(f'Sueldo Basico: {self.sueldoBasico}')
        print(f'Antiguedad: {self.antiguedad}')
        print(f'Porcentaje adicional: {self.porcAdicional}')

def empleadoConMasClientes(listaEmpleados):
    contadorClientesSuperior = 0 
    for empleado in listaEmpleados:
        if empleado.tipoContratacion == CatEmpleado.CAT1.value:
            if empleado.clientesCaptados > contadorClientesSuperior:
                contadorClientesSuperior = empleado.clientesCaptados
                empleadoMasClientes = empleado
    return empleadoMasClientes


empleados = [
    SueldoFijo("14050666", "Maria","Cruz",2002, 100000), # Antiguedad 22
    SueldoFijo("11222", "Leandro", "Torres", 2023, 10000), # Antiguedad 1
    SueldoFijo("129230", "Valeria", "Mendez", 2019, 40000), # Antiguedad 5
    PorComision("102202", "Jose", "Rodriguez", 2023, 10200, 2, 4000),
    PorComision("2039940", "Jesus", "Moreno", 2014, 20000,6,4000),
    PorComision("1020202", "Abril", "Moreno", 2002, 45000,1,4000),
    PorComision("2034022", "Rodrigo", "Paz", 2010,23000,4,1000)
]

for e in empleados:
    e.mostrarEmpleado()
    print("...............")

print("===============================")

for e in empleados:
    e.mostrarSalario()

empConMasClientes = empleadoConMasClientes(empleados)

print("===============================")
print(f'Empleado con más clientes: {empConMasClientes.apellido}, {empConMasClientes.nombre}')