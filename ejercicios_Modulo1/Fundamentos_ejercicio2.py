# Crear una lista de 5 elementos y aplicar:
    # Imprimir el ultimo elemento
    # Modificar el valor del tercer elemento
    # Agregar 2 elementos
    # Eliminar algun elemento

numeros = [2,3,1,6,4,5,19,12]

longitud = len(numeros)

print("El ultimo elemento es: ", numeros[longitud-1])

numeros[2] = 100

numeros.append("veinte")
numeros.append(22)

numeros.pop(3)

print("Lista resultante:\n\t", numeros)