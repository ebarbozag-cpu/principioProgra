#Definir las variables de los examenes
examen1 = 0
examen2 = 0
examen3 = 0
resultado = 0

#Solicitar las notas al profesor

examen1 = float (input( "Ingrese la nota del examen 1:"))
examen2 = float (input( "Ingrese la nota del examen 2:"))
examen3 = float (input( "Ingrese la nota del examen 3:"))

#Se realiza el calculo

resultado = ( examen1 + examen2 + examen3 ) / 3

print ("El resultado es: ",resultado)