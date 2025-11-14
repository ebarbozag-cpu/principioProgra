#Definir Variables

calificacion = 0

#Solicitar entradas

calificacion = int(input("Digite la nota:"))

#Procesos/salidas

if calificacion <= 59 and calificacion >= 0:
    print("Su calificación es una F")
elif calificacion >= 60 and calificacion <= 69:
    print("Su calificacion es una D")
elif calificacion >= 70 and calificacion <= 79:
    print("Su calificacion es una C")
elif calificacion >= 80 and calificacion <= 89:
    print("Su calificacion es una B")
elif calificacion >= 90 and calificacion <= 100:
    print("Su calificacion es una A")
else:
    print("Error,Digite un numero entre 0 y 100")