#Definir Variables

numero = 0

#entradas
try:
    numero = int(input("Digite un número entero:"))

#procesos/salidas

    if numero >= 0 and numero < 20:
        print("El juego está en curso")
    elif numero == 20:
        print("Ha perdido la partida")
    else:
        print("Número inválido; favor ingresar un número valido")
        
except ValueError:
    print("Número inválido; favor ingresar un número valido")

