"""
Este es mi primer programa

"""

#Variables

n1 = 0  #Esto es la variable que almacena el pprimer número.
n2 = 0  #Esto es la variable que almacena el segundo número.
n3 = 0  #Esto es la variable que almacena el tercer número.
resultadoSuma = 0 #Esto es la variable que almacena el resultado de la suma.
resultadoMulti = 0 #Esto es la variable que almacena el resultado de la multiplicación.


#este es una función que realiza la suma y multiplicación de dos numeros
#Entrada de datos se utiliza input()
#Se ingresa int para identicar que es un número entero

print ( "Hola Buenas Tardes" )

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercero número: "))

#Procesamiento de datos se utiliza la variable de suma y se hace la operación

resultadoSuma = n1 + n2 + n3
resultadoMulti = n1 * n2 * n3



#salida de datos se utiliza print()

print ( "El resultado de la suma 2 es:",resultadoSuma )
print ( "El resultado de la multiplicacion de los 3 numeros es", resultadoMulti )

