#Definir Variables

nombre_pais = ""
cantidad_enfermos = 0
cantidad_muertos = 0
tasa_mortalidad = 0.0



#Solicitar entradas

nombre_pais = str(input("Ingrese el pais:"))
cantidad_enfermos = int(input("Ingrese la cantidad de enfermos:"))
cantidad_muertos = int(input("Ingrese la cantidad de muertes:"))



#Procesos

tasa_mortalidad = (cantidad_muertos / cantidad_enfermos) * 100



#Salidas

print("La tasa de mortalidad de",nombre_pais,"corresponde a:",tasa_mortalidad,"%")