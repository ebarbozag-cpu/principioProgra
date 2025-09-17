#Definir Variables

nombre = ""
estatura = 0.0
peso = 0.0
formula_estatura = 0.0
formula_imc = 0.0

#Solicitar entradas

nombre = str(input("Ingrese su nombre:" ))
estatura = float(input("Ingrese su estatura:" ))
peso = float(input("Ingrese su peso actual:" ))

#Realizar operación
formula_estatura = estatura ** 2
formula_imc = peso / formula_estatura


#Salidas
print("Bienvenido al calculador de IMC")
print ("Hola! ",nombre,)
print (f"Su indice de masa corporal es de: {formula_imc:.2f}\n")
print("Gracias por usar el calculador de IMC")