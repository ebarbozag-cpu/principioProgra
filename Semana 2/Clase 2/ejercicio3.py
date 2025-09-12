#Definir Variables

cantidad_noches = 0
descuento = 0
conversion_descuento = 0
costo_habitación = 100
total_noches = 0
monto_total = 0
iva = 13
conversion_iva = 0
monto_pagar_ii = 0

#Solicitar entradas

cantidad_noches = int(input("Ingrese la cantidad de noches:" ))
descuento = int(input("Ingrese el descuento aplicado:" ))

#Realizar operación
total_noches = cantidad_noches * costo_habitación
conversion_descuento = descuento / 100
monto_pagar = total_noches - (total_noches * conversion_descuento)
conversion_iva = iva / 100
monto_pagar_ii = monto_pagar + (monto_pagar * conversion_iva)


#Salidas

print ("El monto total a pagar por la estadia es: $",monto_pagar)
print ("El monto total a pagar por la estadia con ii Incluido es: $",monto_pagar_ii)



