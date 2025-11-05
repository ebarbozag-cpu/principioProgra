# --- Inicio del Programa ---

# 1. Almacenar las siete piezas como variables str (usando un diccionario)
# Se usan comillas triples (""") para definir strings de múltiples líneas.
piezas = {
    'o': """**
**""",
    
    'l': """*
*
*
*""",
    
    's': """ **
**""",
    
    'z': """**
 **""",
    
    'L': """*
*
**""",
    
    'J': """ *
 *
**""",
    
    'T': """***
 *"""
}

# 2. Recibir el dato del usuario
entrada_usuario = input("Introduce el carácter de la pieza (o, l, s, z, L, J, T): ")

# 3. Evaluar la entrada
# Primero, validamos que sea un *único* carácter.
if len(entrada_usuario) != 1:
    print("El dato de entrada no es válido.")

# Segundo, verificamos si ese carácter es una de nuestras piezas válidas
elif entrada_usuario in piezas:
    # Si está en el diccionario, imprime su valor (la forma)
    print(piezas[entrada_usuario])

else:
    # Si tiene longitud 1, pero no está en el diccionario (ej: 'a', '5')
    print("El dato de entrada no es válido.")

# --- Fin del Programa ---