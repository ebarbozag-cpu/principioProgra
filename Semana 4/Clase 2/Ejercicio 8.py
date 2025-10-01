#Definir Variables

lado_1 = 0
lado_2 = 0
lado_3 = 0

#Solicitar entradas

lado_1 = int(input("Digite el lado 1:"))
lado_2 = int(input("Digite el lado 2:"))
lado_3 = int(input("Digite el lado 3:"))

#Procesos/salidas

if lado_1 == lado_2 and lado_2 == lado_3:
    print("El triangulo es un Equilatero")
elif lado_1 != lado_2 and lado_2 == lado_3:
    print("El triangulo es un Isósceles")
elif lado_2 != lado_1 and lado_1 == lado_3:
    print("El triangulo es un Isósceles")
elif lado_3 != lado_2 and lado_2 == lado_1:
    print("El triangulo es un Isósceles")
else:
    lado_1 != lado_2 and lado_2 != lado_3
    print("El triangulo es un Escaleno")


