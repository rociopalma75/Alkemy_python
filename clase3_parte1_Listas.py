# ESTRUCTURAS DE CONTROL : While - For
# COLECCIONES DE DATOS
    #Listas - ArrayList

# LISTAS
nombres = ["Juan", "Pepe", "Luis"]
names = ["John","Mary", "Dean", "Zendaya", "Matthew"]

print(nombres)

# Acceder a un elemento de la lista
print(nombres[2])

# Mutable
# nombres = [1,2,3,4] # Le reasigne datos nuevos

# nombres = False # Incluso no necesariamente tiene que ser una lista 

# Métodos para calcular listas

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

# reverse -> invertir el orden de la lista (sea cual sea)
numeros.reverse()
print(numeros)

