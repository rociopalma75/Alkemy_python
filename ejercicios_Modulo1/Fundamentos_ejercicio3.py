# Crear funcion llamada verificar_calificacion que recibe 3 parametros
    # nota1,nota2,nota3
    # Dentro de la funcion calcular el promedio de las notas
    # Si el promedio es mayor o igual a 6, entonces la funcion debe retornar un mensaje "Aprobado", en caso contrario "Reprobado"

def verificar_Calificacion(nota1,nota2,nota3):
    promedio = (nota1 + nota2 + nota3)/3
    if promedio >= 6:
        return "APROBADO"
    else:
        return "DESAPROBADO"
    
nota1 = float(input("Ingrese la 1ra nota: "))
nota2 = float(input("Ingrese la 2da nota: "))
nota3 = float(input("Ingrese la 3ra nota: "))

print(f'Nota final: {verificar_Calificacion(nota1,nota2,nota3)}')
