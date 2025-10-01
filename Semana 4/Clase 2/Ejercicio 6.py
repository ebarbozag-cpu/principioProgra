#Definir Variables

numero_1 = 0
numero_2 = 0
operacion = 0


#Solicitar entradas

print("Menú de opciones:")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")
operacion = int(input("Que operacion desea realizar: "))
numero_1 = int(input("Digite el primer número: "))
numero_2 = int(input("Digite el segundo número: "))

#Procesos/salidas

if operacion == 1:
    print("El resultado de la suma es", numero_1 + numero_2)
elif operacion == 2:
    print("El resultado de la resta es", numero_1 - numero_2)
elif operacion == 3:
    print("El resultado de la multiplicación es", numero_1 * numero_2)
elif operacion == 4:
    print("El resultado de la división es", numero_1 / numero_2)
else:
    print("No digitó un número válido del menú")