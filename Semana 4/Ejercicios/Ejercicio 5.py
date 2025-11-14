#Definir Variables

precio_compra = 0.0

#Solicitar entradas


precio_compra = float(input("Ingrese el monto de la compra:"))


#Procesos/salidas

if  precio_compra > 100.00:
        print("La compra con un descuento aplicado es de: ", precio_compra - (precio_compra * (10 / 100)))
else:
        print("El precio de compra no superó los $100, por lo tanto no tiene descuento. Precio final:", precio_compra)
