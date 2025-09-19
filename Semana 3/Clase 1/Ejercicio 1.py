#Definir Variables

nombre_producto = ""
precio_producto = 0.0
precio_final = 0.0

#Solicitar entradas

nombre_producto = str(input("Ingrese el nombre del producto:"))
precio_producto = float(input("Ingrese el precio del producto:"))

#Realizar operación

precio_final = precio_producto + ((13 / 100) * precio_producto)

#Salidas

print("El precio del producto ",nombre_producto, "es de",precio_final)