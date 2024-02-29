# LISTAS, TUPLAS y DICCIONARIOS

# =================LISTAS================= (MUTABLES)

nombres = ["Juan", "Pepe", "Luis"]
names = ["John","Mary", "Dean", "Zendaya", "Matthew"]

# Acceder a un elemento de la lista
print(nombres[2])

# nombres = [1,2,3,4] # Le reasigne datos nuevos
# nombres = False # Incluso no necesariamente tiene que ser una lista 

#Append -> agrega al FINAL de la lista
nombres.append("Lucia")
print(nombres)

# insert -> agrega en el INDICE indicado de la lista
nombres.insert(2,"Joel")
print(nombres)

# pop -> elimina un elem al FINAL de la lista o en el INDICE indicado
    # pop() -> al final de la lista
    # pop(indice) -> la posición indice

nombres.pop()
print(nombres)

nombres.pop(3)
print(nombres)

# remove -> elimina un elem si consigue el elem especifico
    # remove(elem) -> elimina elem
    # remove elimina la primera ocurrencia que encuentra
nombres.remove("Pepe")
print(nombres)

# extend -> añadir una lista a otra preexistente
    # lista1.extend(lista2) -> a la lista1 se le agrega todos los elementos de la lista 2
nombres.extend(names)
print(nombres)

numeros = [233,4,3,56,799,90,67,33,87]
print(numeros)

# sort -> ordena la lista de menor a mayor
# numeros.sort()
print(numeros)

#Invierte el orden de la lista (sea cual sea)
numeros.reverse()
print(numeros)

# =================TUPLAS=================

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

# =================DICCIONARIOS=================

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
