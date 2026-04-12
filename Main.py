from datos_productos import cargar_catalogo
from operacion import Carrito

class ContiMusicApp:
    def __init__(self):
        self.inventario = cargar_catalogo()
        self.carrito = Carrito()

    def mostrar_menu(self):
        while True:
            print("\n" + "="*35)
            print("   CONTIMUSIC POS - GRUPO D")
            print("="*35)
            print("1. Ver Catálogo")
            print("2. Registrar Venta")
            print("3. Generar Boleta")
            print("4. Salir")
            
            opcion = input("Seleccione: ")
            
            if opcion == "1":
                print("\n--- INVENTARIO DISPONIBLE ---")
                for prod in self.inventario: print(prod)
            elif opcion == "2":
                self.ejecutar_venta()
            elif opcion == "3":
                self.imprimir_comprobante()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break

    def ejecutar_venta(self):
        try:
            id_p = int(input("Ingrese ID del producto: "))
            prod = next((p for p in self.inventario if p.id == id_p), None)
            if prod:
                cant = int(input(f"Cantidad de {prod.nombre}: "))
                if self.carrito.agregar(prod, cant):
                    print("✅ Producto añadido.")
                else:
                    print("❌ Error: Stock insuficiente.")
            else:
                print("❌ Error: El ID no existe.")
        except ValueError:
            print("❌ Error: Entrada no válida.")

    def imprimir_comprobante(self):
        sub, igv, tot = self.carrito.calcular_totales()
        if sub == 0:
            print("\nEl carrito está vacío.")
            return
        print("\n" + "*"*30)
        print("      BOLETA DE VENTA")
        print("*"*30)
        for i in self.carrito.items:
            print(f"{i['nombre']} x{i['cantidad']}: S/ {i['subtotal']:.2f}")
        print("-" * 30)
        print(f"SUBTOTAL:  S/ {sub:.2f}")
        print(f"IGV (18%): S/ {igv:.2f}")
        print(f"TOTAL:     S/ {tot:.2f}")
        print("*"*30)

if __name__ == "__main__":
    app = ContiMusicApp()
    app.mostrar_menu()