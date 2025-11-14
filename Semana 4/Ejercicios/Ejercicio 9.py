#Definir Variables

temperatura = 0

#Solicitar entradas

temperatura = int(input("Digite la temperatura:"))

#Procesos/salidas

if temperatura < 0:
    print("La temperatura está en Frio extremo")
elif temperatura >= 0 and temperatura <= 30:
    print("El clima es Templado")
else:
    temperatura >= 30
    print("La temperatura está en calor intenso")

