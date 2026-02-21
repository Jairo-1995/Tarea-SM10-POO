# main.py
from servicios.inventario import Inventario

def main():
    inventario = Inventario()
    # menu interactivo para gestionar el inventario de productos amazónicos
    while True:
        print("\n--- Sistema de Gestión de Inventarios (Productos Amazónicos) ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario completo")
        print("6. Salir")
        
        opcion = input("Selecciona una opción : ").strip()
        
        if opcion == "1":
            # Añadir producto
            id = input("ID único: ").strip()
            nombre = input("Nombre del producto (ej. Aguaje, Cacao): ").strip()
            categoria = input("Categoría del producto (ej. Frutas, Semillas): ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio por unidad: "))
                inventario.añadir_producto(id, nombre, categoria, cantidad, precio)
            except ValueError:
                print("Error: Cantidad y precio deben ser números.")
        
        elif opcion == "2":
            #---- Eliminar producto -----
            id = input("ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id)
        
        elif opcion == "3":
            # ---- -Actualizar producto -----
            id = input("ID del producto a actualizar: ").strip()
            print("Deja en blanco si no quieres cambiar:")
            categoria_str = input("Nueva categoría: ").strip()
            cantidad_str = input("Nueva cantidad: ").strip()
            precio_str = input("Nuevo precio: ").strip()
            nueva_categoria = categoria_str if categoria_str else None
            nueva_cantidad = int(cantidad_str) if cantidad_str else None
            nuevo_precio = float(precio_str) if precio_str else None
            inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio, nueva_categoria)
        
        elif opcion == "4":
            # ---- Buscar producto ----
            nombre_parcial = input("Nombre del producto a buscar: ").strip()
            inventario.buscar_productos(nombre_parcial)
        
        elif opcion == "5":
            # Mostrar inventario
            inventario.mostrar_inventario()
        
        elif opcion == "6":
            # Salir
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()