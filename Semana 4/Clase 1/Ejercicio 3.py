
#Definir Variables
nota = 0

#Solicitar entradas
try:
    nota = int (input("Digite la nota del estudiante:"))

#Procesos/salidas

    if nota >= 70 and nota <= 100:
        print("El estudiante aprobó")
    elif nota >= 0 and nota <= 69:
        print("El estudiante reprobó")
    else:
        print("Error: La nota debe ser un número entero entre 0 y 100")
except:
    print("Error: Entrada inválida. Por favor, ingrese un número entero.")

