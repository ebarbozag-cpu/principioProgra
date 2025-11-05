# ======================================================
# Ejercicio de Programación: Sistema Básico de Restaurante
# ======================================================

# --- 1. Creación del Restaurante ---
# Guardamos el nombre y el menú en las estructuras que decidimos.
nombre_res = "Emafood"
menu = {
    "Pizza": 15,
    "Pasta": 12,
    "Ensalada": 8
}
# La lista para guardar todos los pedidos empieza vacía.
ordenes = []

print(f"¡Bienvenido a {nombre_res}!")

# --- 2. Menú Interactivo ---
# Un bucle 'while True' se repetirá para siempre hasta que elijamos salir.
while True:
    print("\n--- Menú de Gestión ---")
    print("1. Añadir un nuevo pedido")
    print("2. Actualizar estado de un pedido")
    print("3. Ver todos los pedidos activos")
    print("4. Salir")
    
    opcion = input("Por favor, elige una opción: ")

    # --- 3. Gestión de Órdenes (Añadir) ---
    if opcion == '1':
        print("\n--- Menú de Platillos ---")
        # Mostramos el menú al cliente para que sepa qué pedir
        for platillo, precio in menu.items():
            print(f"- {platillo}: ${precio}")
        
        platillos_del_pedido = []
        while True:
            platillo_elegido = input("Añade un platillo a la orden (o escribe 'fin' para terminar): ")
            if platillo_elegido.lower() == 'fin':
                break
            # Verificamos si el platillo existe en nuestro menú
            if platillo_elegido in menu:
                platillos_del_pedido.append(platillo_elegido)
                print(f"'{platillo_elegido}' añadido a la orden.")
            else:
                print("Ese platillo no está en el menú, intenta de nuevo.")
        
        # Solo creamos la orden si el cliente eligió al menos un platillo
        if platillos_del_pedido:
            nueva_orden = {
                "platillos": platillos_del_pedido,
                "estado": "Iniciado"
            }
            ordenes.append(nueva_orden)
            print("¡Orden creada con éxito!")

    # --- 4. Gestión de Órdenes (Actualizar Estado) ---
    elif opcion == '2':
        if not ordenes:
            print("No hay pedidos activos para actualizar.")
            continue # Vuelve al inicio del bucle 'while'

        # Mostramos las órdenes con un número para que el usuario elija
        print("\n--- Pedidos Activos ---")
        for i, orden in enumerate(ordenes):
            print(f"[{i}] - Platillos: {', '.join(orden['platillos'])} | Estado: {orden['estado']}")
        
        try:
            indice_orden = int(input("Ingresa el número del pedido que quieres actualizar: "))
            
            # Verificamos que el número sea válido
            if 0 <= indice_orden < len(ordenes):
                orden_a_actualizar = ordenes[indice_orden]
                print(f"\nEstado actual: {orden_a_actualizar['estado']}")
                print("Elige el nuevo estado:")
                print(" a. En preparación")
                print(" b. Finalizado")
                
                nuevo_estado_opcion = input("Opción: ").lower()
                
                if nuevo_estado_opcion == 'a':
                    orden_a_actualizar['estado'] = "En preparación"
                    print("¡Estado actualizado a 'En preparación'!")
                elif nuevo_estado_opcion == 'b':
                    # --- 5. Finalización de la Orden ---
                    orden_a_actualizar['estado'] = "Finalizado"
                    
                    # Calculamos el total usando el bucle 'for' que diseñamos
                    total_a_pagar = 0
                    for platillo in orden_a_actualizar['platillos']:
                        total_a_pagar += menu[platillo] # Buscamos el precio en el menú
                    
                    print(f"\n¡Orden Finalizada! Total a pagar: ${total_a_pagar}")
                    
                    # Eliminamos la orden de la lista
                    ordenes.pop(indice_orden)
                    print("La orden ha sido pagada y eliminada de la lista de activos.")
                else:
                    print("Opción no válida.")
            else:
                print("Número de pedido fuera de rango.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

    elif opcion == '3':
        if not ordenes:
            print("\nNo hay ningún pedido activo en este momento.")
        else:
            print("\n--- Todos los Pedidos Activos ---")
            for i, orden in enumerate(ordenes):
                # Usamos join para mostrar la lista de platillos de forma más legible
                lista_platillos = ", ".join(orden['platillos'])
                print(f"[{i}] - Platillos: {lista_platillos} | Estado: {orden['estado']}")

    elif opcion == '4':
        print("Gracias por usar el sistema de Emafood. ¡Hasta luego!")
        break # 'break' es el comando que rompe el bucle 'while' y termina el programa.
    
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")