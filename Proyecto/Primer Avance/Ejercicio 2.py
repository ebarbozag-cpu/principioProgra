#Definir Variables

cantidad_lineas = 0
resultado = 0
n = cantidad_lineas

#entradas
try:
    cantidad_lineas = int(input("Digite un número entero:"))

#procesos/salidas

    if cantidad_lineas >= 0 and cantidad_lineas <= 50:
        n = cantidad_lineas
        resultado = 2.5 * n * (n + 1)
        print(f"Su puntaje acumulado es de {resultado} puntos")
    else:
        print("Número inválido; favor ingresar un número valido")
        
except ValueError:
    print("Número inválido; favor ingresar un número valido")