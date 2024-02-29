# BUCLE FOR y FUNCIONES

# =================BUCLE FOR=================

nombres = ["Tito", "Juan", "Pepe", "Martina", "Luis"]

#Por cada elemento "nombre" en la lista "nombres"...
for nombre in nombres:
    print(nombre)

print("=============================")
# For in en tuplas
diasSemana = (
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado", 
    "Domingo",
    "Lunes"
)

for dia in diasSemana:
    print(dia)

print("=============================")
# FOR IN en DICCIONARIO
    
persona1 = {
    "nombre":"Rocio",
    "apellido":"Palma",
    "edad":21,
    "altura": 1.67
}

for elem in persona1:
    print(elem)
    #Devuelve las keys

print("................")

for elem in persona1.values():
    print(elem)
    #Devuelve valores

print("................")

for elem in persona1.items():
    print(elem)
    #Devuelve las tuplas key-value

print("................")

for dato in persona1.items():
    for elem in dato:
        print(elem)

# =================FUNCIONES=================

def sumar_iva(precio, porIva = 1.21):
    print(precio*porIva)


sumar_iva(2500,1)
sumar_iva(1090)


# ALGORITMOS. Son un conjunto de instrucciones que reciben info del exterior, la procesas y luego devuelven el resultado del proceso
    # 1. ENTRADA DE DATOS
    # 2. PROCESAMIENTO DE DATOS
    # 3. RETORNO DE DATOS

