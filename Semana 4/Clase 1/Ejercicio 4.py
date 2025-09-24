#Definir Variables

edad = 0

#Solicitar entradas

try:
    edad = int(input("Digite la edad de la persona:"))

#Procesos/salidas

    if edad >= 1 and edad <= 12:
        print("La persona es un niño")
    elif edad >= 13 and edad <= 17:
        print("La persona es un adolecente")
    elif edad >=18:
        print("La persona es un adulto")
    else:
        print("Digite una entrada valida")
except:
    print("Error: Entrada inválida. Por favor, ingrese un número entero.")