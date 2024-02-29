from os import system

def suma(num1, num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

i = 1

while i == 1 :
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    
    eleccion = input("Ingresar la accion \n\tA-> suma \n\tB-> resta \n\tRespuesta: ")

    if eleccion == "A" or eleccion == 'a':
        print(f'El resultado de {num1} + {num2} = {suma(num1,num2)}')
    elif eleccion == 'B' or eleccion == 'b':
        print(f'El resultado de {num1} - {num2} = {resta(num1,num2)}')
    else:
        print("Ingreso una opcion incorrecta")

    
    respuestaUsuario = input("Desea seguir operando: \n\tIngrese 0 -> No \n\tIngrese 1 -> SI \n\tRespuesta: ")
    i = int(respuestaUsuario)

    system("cls")