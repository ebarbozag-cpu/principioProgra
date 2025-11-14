#Definir Variables

numero_1 = 0
numero_2 = 0

#Solicitar entradas

numero_1 = int (input("Digite el primer número: "))
numero_2 = int (input("Digite el segundo número: "))

#Procesos/salidas

if numero_1 > numero_2:
    print(f"el número {numero_1} es mayor que el número {numero_2}")
elif numero_1 == numero_2:
    print(f"el número {numero_1} es igual que el número {numero_2}")
else:
    print(f"el número {numero_2} es mayor que el número {numero_1}")