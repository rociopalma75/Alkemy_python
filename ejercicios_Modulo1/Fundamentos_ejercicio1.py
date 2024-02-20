# Crear un algoritmo para calcular la sumatoria de los primeros cien numeros (del 01 al 100)
i=1
acumulador = 0

while i<=100:
    acumulador += i
    i += 1

print("Resultado de sumar los 100 primeros numeros: ", acumulador)