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

# count - devuelve la cantidad de veces que un elem aparece en la tupla
print(diasSemana.count("Lunes")) 

# index -> devuelve la posición del elem en cuestión
print(diasSemana.index("Viernes"))

#DICCIONARIOS
persona1 = {
    "nombre":"Rocio",
    "apellido":"Palma",
    "edad":21,
    "altura": 1.67
}

print(persona1)

# Metodo keys -> Extrae solamente CLAVES
    #Devuelve una lista
print(persona1.keys())

# Metodo values -> Extrae solamente VALORES
    #Devuelve una lista
print(persona1.values())

#Metodo items -> Extrae en tupla KEY,VALUE
    #Devuelve una lista donde los elementos son tuplas
print(persona1.items())

#Metodo get -> devuelve un elemento con su key/ si no lo encuentro devuelve DEFAULT
resultado = persona1.get('apellido')
print(resultado)

print(persona1.get('legajo'))

# Eliminar elementos de mi diccionario
    # pop -> a traves de su key

persona1.pop('apellido')
print(persona1)

# Metodo clear. Vacia el diccionario
persona1.clear()
print(persona1)
