#Escribir un programa que imprima un mensaje final; solo si el usuario digita un 0


menu = "Bienvenido a mi sistema" \
"1. Para registrar usuario\n" \
"2. Para Modificar usuario\n" \
"3. Para eliminar usuario\n" \
"0. Para salir"

print(menu)

opcion = int(input("\nIngrese una opcion del menu: "))

while opcion != 0:
    if opcion == 1:
        print("Registrando usuario...")
    elif opcion == 2:
        print("Modificando usuario...")
    elif opcion == 3:
        print("Eliminando usuario...")
    else:
        print("Opción invalida")
    opcion = int(input("Escriba una opcion o digite 0 para salir: "))
print("Ganamos! Salimos del ciclo!")










numero = input("Ingrese el número entero")

while contador < len(numero):
    suma_numero += int(numero[contador])
    contador += 1
print(f"La suma de los digitos del número {numero} es:", suma_numero)



# for i in range(5):
#     salario = float(input(f"Digite el salario del empleado {i+1}:"))
#     salario_total += salario

# #salidas

# print(f"El salario total de los  empleados es:", salario_total)
