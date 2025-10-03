


numero = int(input("Digite un número entero (0 para salir):"))
numero_mayor = 0
while numero != 0:
    if numero > numero_mayor:
        numero_mayor = numero
    numero = int(input("Digite un número entero (0 para salir):"))

print(f"El número mayor es:", numero_mayor)

