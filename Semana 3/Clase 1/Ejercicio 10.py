#Definir Variables

precio_original= 0.0
descuento = 0.15

#Solicitar entradas

precio_original = float(input("Ingrese el precio original del producto: "))


#Procesos

descuento = precio_original * descuento
precio_final = precio_original - descuento


#Salidas

print("\n--- Desgloce Costos Almuerzo ---")
print(f"Precio Original: {precio_original:.2f}")
print(f"Descuento aplicado: {descuento:.2f}")
print(f"Precio Final: {precio_final:.2f}")
