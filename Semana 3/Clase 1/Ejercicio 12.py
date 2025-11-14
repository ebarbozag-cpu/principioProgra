#Definir Variables

tafifa_hora= 0.0
hora_entrada= 0
hora_salida= 0 

#Solicitar entradas

tafifa_hora = float(input("Ingrese la tarifa por hora: "))
hora_entrada = int(input("Ingrese la hora de entrada :"))
hora_salida = int(input("Ingrese la hora de salida :"))

#Procesos

horas_trabajadas = hora_salida - hora_entrada
pago_total = horas_trabajadas * tafifa_hora


#Salidas

print("\n--- Resumen ---")
print(f"Hora de Entrada:    {hora_entrada}:00")
print(f"Hora de Salida:     {hora_salida}:00")
print(f"Horas Trabajadas:   {horas_trabajadas} horas")
print(f"Tarifa por Hora:    ${tafifa_hora:.2f}")
print(f"Salario Ganado Hoy: ${pago_total:.2f}")