#TIPOS DE DATOS
    #NUMERICOS
        #int
        #float

numInt = 46
numFloat = 32.6

#TEXTO
saludo = "Bienvenido"

#BOOLEAN
esEstudiante = True

num1 = 23
num2 = 54

#Operadores aritmeticos
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)
print(num1 // num2) #Division entera, trunca el resultado (int)
print(num1 % num2) #Modulo 
print(num1 ** 2) #Exponencial

#Asignación (=)
numero = 20

#Comparacion (==)
print(numero  == 20)

# Distinto que (!=)
# <,>, <=,>=, -> solo para datos numericos (float o int)

#Abreviaciones += - -=
numero += 1

saludo = "hola"
saludo += " mundo"
print(saludo)

#Operadores logicos
edad = 10
print((edad >= 13) and (edad <= 17))


nombre = "rocio"
apellido = "palma"

# f string -> convina texto estatico con variables
nombreCompleto = f'{nombre} {apellido}'
print(nombreCompleto)
mensaje = f'Hola mi nombre es {nombreCompleto} y tengo {edad} aa'
print(mensaje)

#ESTRUCTURAS CONDICIONALES
if(edad >= 18):
    print(f'Tenes {edad}, podes pasar al boliche')
elif((edad >= 13) and (edad <= 17)):
    print(f'Tenes {edad}, no podes ir al boliche, pero si a la matine')
else:
    print(f'Tenes {edad}, no podes pasar a nada')    