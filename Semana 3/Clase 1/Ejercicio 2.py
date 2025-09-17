#Definir Variables

km_inicio = 0
km_fin = 0
km_suma = 0
km_total = 0

#Solicitar entradas

km_inicio = int(input("Ingrese el kilometraje inicial:" ))
km_fin = int(input("Ingrese el kilometraje final:" ))

#Realizar operación

km_suma = km_inicio - km_fin
km_total = km_suma + km_inicio

#Salidas

print("El kilometraje total es de: ",km_total)