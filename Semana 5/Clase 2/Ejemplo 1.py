#Definir Variables

salario_total = 0.0
salario = 0.0

#entradas/procesos

for i in range(5):
    salario = float(input(f"Digite el salario del empleado {i+1}:"))
    salario_total += salario

#salidas

print(f"El salario total de los  empleados es:", salario_total)
