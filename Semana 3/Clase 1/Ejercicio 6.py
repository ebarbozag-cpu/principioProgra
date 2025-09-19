#Definir Variables

porcentaje_impuesto = 0.0
salario_bruto = 0.0
salario_neto = 0.0


#Solicitar entradas

salario_bruto = float(input("Ingrese el salario bruto:"))
porcentaje_impuesto = float(input("Ingrese el impuesto a aplicar:"))

#Procesos

salario_neto = salario_bruto - ((porcentaje_impuesto / 100) * salario_bruto)


#Salidas

print("El salario neto a pagar es",salario_neto)