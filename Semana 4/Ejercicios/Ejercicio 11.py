#Definir Variables

dia = 0

#Solicitar entradas

dia = int(input("Digite un número entre 1 y 7 para saber el día de la semana:"))

#Procesos/salidas

if dia == 1:
    print("El día es Lunes")
elif dia == 2:
    print("El día es martes")
elif dia == 3:
    print("El día es miercoles")
elif dia == 4:
    print("El día es jueves")
elif dia == 5:
    print("El día es viernes")
elif dia == 6:
    print("El día es sabado")
elif dia == 7:
    print("El día es domingo")
else:
    print("Digite un número entre 1 y 7")