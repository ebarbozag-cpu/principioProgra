#Definir Variables

ganancia_limonada = 4.5
limonadas_vendidas = 0
monto_ganado = 0
ganancia_hugo = 0.0
ganacia_pacoyluis = 0.0

#Solicitar entradas

limonadas_vendidas = int(input("Digite la cantidad de limonadas vendidas:"))


#Procesos

monto_ganado = limonadas_vendidas * ganancia_limonada
ganacia_pacoyluis = (monto_ganado  * 0.60) /2
ganancia_hugo = monto_ganado * 0.40


#Salidas

print("Ganancia de Hugo:",ganancia_hugo)
print("Ganancia de Paco:",ganacia_pacoyluis)
print("Ganancia de Luis:",ganacia_pacoyluis)

