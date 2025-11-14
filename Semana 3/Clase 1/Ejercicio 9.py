#Definir Variables

costo_total= 2700
porcentaje_pan= 0.15
porcentaje_tomate= 0.35
porcentaje_queso= 0.25
porcentaje_lechuga= 0.10
porcentaje_total= 1.0

#Procesos

porcentaje_jamon= porcentaje_total - (porcentaje_pan + porcentaje_tomate + porcentaje_queso + porcentaje_lechuga)
cost_pan= costo_total * porcentaje_pan
cost_tomate= costo_total * porcentaje_tomate
cost_queso= costo_total * porcentaje_queso
cost_lechuga= costo_total * porcentaje_lechuga
cost_jamon= costo_total * porcentaje_jamon

#Salidas

print("--- Desgloce Costos Almuerzo ---")
print(f"Costo Pan: {cost_pan:.2f}")
print(f"Costo Tomate: {cost_tomate:.2f}")
print(f"Costo Queso: {cost_queso:.2f}")
print(f"Costo Lechuga: {cost_lechuga:.2f}")
print(f"Costo Jamón: {cost_jamon:.2f}")
print(f"Costo Total Almuerzo: {costo_total:.2f}")

