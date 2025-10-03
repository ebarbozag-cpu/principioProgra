#Se va a recibir un número entero , y obtener la suma total de sus digitos
#123 -> 1+2+3 = 6

numero = int(input("Ingrese un numero entero: "))
suma_digitos = 0
# 123 -> 3
x = numero % 10
while numero > 0:
    suma_digitos += x
    numero = numero // 10
    x = numero % 10
print(suma_digitos)

# # numero = input("Ingrese un numero entero: ")
# # suma_digitos = 0

# # if numero.isdigit():
# #     for i in range(len(numero)):
# #         suma_digitos += int(numero[i])
# #     print(suma_digitos)
# # else:
# #     print("No es un numero entero")








# #Definir Variables

# suma_numero = 0
# numero = 0
# contador = 0
# #entradas/procesos

# numero = input("Ingrese el número entero")

# while contador < len(numero):
#     suma_numero += int(numero[contador])
#     contador += 1
# print(f"La suma de los digitos del número {numero} es:", suma_numero)



# # for i in range(5):
# #     salario = float(input(f"Digite el salario del empleado {i+1}:"))
# #     salario_total += salario

# # #salidas

# # print(f"El salario total de los  empleados es:", salario_total)
