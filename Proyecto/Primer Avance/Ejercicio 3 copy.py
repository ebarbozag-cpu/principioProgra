class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.platillos = {}
        self.ordenes = []
        self.contador_ordenes = 1
        
    def agregar_platillo(self, nombre, precio, stock=float('inf')):
        """Agrega un platillo al menú del restaurante"""
        self.platillos[nombre] = {
            'precio': precio,
            'stock': stock
        }
    
    def mostrar_menu(self):
        """Muestra el menú disponible"""
        print(f"\n--- MENÚ DEL RESTAURANTE {self.nombre.upper()} ---")
        for i, (platillo, info) in enumerate(self.platillos.items(), 1):
            stock_info = f" (Stock: {info['stock']})" if info['stock'] != float('inf') else ""
            print(f"{i}. {platillo} - ${info['precio']:.2f}{stock_info}")
    
    def crear_orden(self):
        """Crea una nueva orden"""
        if not self.platillos:
            print("No hay platillos disponibles en el menú.")
            return
        
        self.mostrar_menu()
        orden_platillos = []
        
        while True:
            try:
                seleccion = input("\nSelecciona un platillo (número) o '0' para terminar: ")
                if seleccion == '0':
                    break
                
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(self.platillos):
                    platillo = list(self.platillos.keys())[seleccion - 1]
                    
                    # Verificar stock
                    if self.platillos[platillo]['stock'] <= 0:
                        print(f" {platillo} agotado")
                        continue
                    
                    # Reducir stock si es limitado
                    if self.platillos[platillo]['stock'] != float('inf'):
                        self.platillos[platillo]['stock'] -= 1
                    
                    orden_platillos.append(platillo)
                    print(f"✅ {platillo} agregado a la orden")
                else:
                    print("Selección inválida")
            except ValueError:
                print("Por favor ingresa un número válido")
        
        if orden_platillos:
            orden = {
                'id': self.contador_ordenes,
                'platillos': orden_platillos,
                'estado': 'Iniciado',
                'total': self._calcular_total(orden_platillos)
            }
            self.ordenes.append(orden)
            self.contador_ordenes += 1
            print(f"\n✅ Orden #{orden['id']} creada exitosamente")
            print(f"Platillos: {', '.join(orden_platillos)}")
            print(f"Estado: {orden['estado']}")
        else:
            print("No se agregaron platillos a la orden")
    
    def _calcular_total(self, platillos):
        """Calcula el total de una orden"""
        total = 0
        for platillo in platillos:
            total += self.platillos[platillo]['precio']
        return total
    
    def mostrar_ordenes(self):
        """Muestra todas las órdenes activas"""
        if not self.ordenes:
            print("\nNo hay órdenes activas")
            return
        
        print(f"\n--- ÓRDENES ACTIVAS EN {self.nombre.upper()} ---")
        for orden in self.ordenes:
            print(f"Orden #{orden['id']}:")
            print(f"  Platillos: {', '.join(orden['platillos'])}")
            print(f"  Estado: {orden['estado']}")
            print(f"  Total: ${orden['total']:.2f}")
            print("-" * 30)
    
    def cambiar_estado_orden(self):
        """Cambia el estado de una orden"""
        if not self.ordenes:
            print("No hay órdenes para modificar")
            return
        
        self.mostrar_ordenes()
        
        try:
            orden_id = int(input("\nIngresa el número de orden a modificar: "))
            orden = next((o for o in self.ordenes if o['id'] == orden_id), None)
            
            if not orden:
                print("Orden no encontrada")
                return
            
            print(f"\nOrden actual: {orden['estado']}")
            print("Estados disponibles:")
            print("1. Iniciado")
            print("2. En preparación")
            print("3. Finalizado")
            
            nuevo_estado = input("Selecciona el nuevo estado (1-3): ")
            
            if nuevo_estado == '1':
                orden['estado'] = 'Iniciado'
                print("✅ Estado cambiado a 'Iniciado'")
            elif nuevo_estado == '2':
                orden['estado'] = 'En preparación'
                print("✅ Estado cambiado a 'En preparación'")
            elif nuevo_estado == '3':
                orden['estado'] = 'Finalizado'
                print(f"\n🎉 Orden #{orden['id']} finalizada!")
                print(f"Platillos: {', '.join(orden['platillos'])}")
                print(f"TOTAL A PAGAR: ${orden['total']:.2f}")
                
                # Eliminar orden finalizada
                self.ordenes = [o for o in self.ordenes if o['id'] != orden_id]
                print("✅ Orden eliminada del sistema")
            else:
                print("Opción inválida")
                
        except ValueError:
            print("Por favor ingresa un número válido")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del restaurante"""
        print(f"\n--- ESTADÍSTICAS DE {self.nombre.upper()} ---")
        print(f"Total de platillos en menú: {len(self.platillos)}")
        print(f"Órdenes activas: {len(self.ordenes)}")
        
        # Mostrar stock de platillos
        print("\nStock de platillos:")
        for platillo, info in self.platillos.items():
            if info['stock'] != float('inf'):
                print(f"  {platillo}: {info['stock']} disponibles")

def main():
    # Crear el restaurante
    print("=== SISTEMA DE RESTAURANTE ===")
    nombre_restaurante = input("Ingresa el nombre del restaurante: ")
    restaurante = Restaurante(nombre_restaurante)
    
    # Agregar platillos iniciales
    print("\nConfiguración de platillos iniciales:")
    platillos_iniciales = [
        ("Hamburguesa", 8.99, 10),
        ("Pizza", 12.50, 8),
        ("Ensalada", 6.75, 15)
    ]
    
    for nombre, precio, stock in platillos_iniciales:
        restaurante.agregar_platillo(nombre, precio, stock)
    
    print("✅ Platillos iniciales configurados")
    
    # Menú principal
    while True:
        print(f"\n=== RESTAURANTE {restaurante.nombre.upper()} ===")
        print("1. Ver menú")
        print("2. Crear nueva orden")
        print("3. Ver órdenes activas")
        print("4. Cambiar estado de orden")
        print("5. Ver estadísticas")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción (1-6): ")
        
        if opcion == '1':
            restaurante.mostrar_menu()
        elif opcion == '2':
            restaurante.crear_orden()
        elif opcion == '3':
            restaurante.mostrar_ordenes()
        elif opcion == '4':
            restaurante.cambiar_estado_orden()
        elif opcion == '5':
            restaurante.mostrar_estadisticas()
        elif opcion == '6':
            print("¡Gracias por usar el sistema del restaurante!")
            break
        else:
            print("Opción inválida. Por favor selecciona 1-6.")

if __name__ == "__main__":
    main()