from Producto import Producto
from DetalleOrdenCompra import DetalleOrdenCompra
from OrdenCompra import OrdenCompra

def mostrar_menu():
    print("MENÚ ORDENES DE COMPRA")
    print("a Ver Órdenes de Compra Cargadas")
    print("b Cargar 1 o más Órdenes de Compra")
    print("c Generar Archivo de Orden de Compra por número")
    print("d Salir")

def ver_ordenes(ordenes):
    if not ordenes:
        print("No hay órdenes cargadas.")
        return
    for orden in ordenes:
        print(" " + str(orden))

def cargar_orden():
    orden = OrdenCompra()
    print(f"\nCargando nueva Orden N° {orden.numero}")

    while True:
        print("\n--- Cargar producto ---")
        codigo = input("Código del producto: ")
        denominacion = input("Denominación: ")
        rubro = input("Rubro: ")
        marca = input("Marca: ")
        precio = float(input("Precio de compra: "))
        cantidad = int(input("Cantidad: "))

        prod = Producto(codigo, denominacion, rubro, marca, precio)
        detalle = DetalleOrdenCompra(prod, cantidad)
        orden.agregar_detalle(detalle)

        continuar = input("¿Agregar otro producto? (s/n): ").lower()
        if continuar != "s":
            break

    print(f"\nOrden N° {orden.numero} cargada correctamente. Total: ${orden.total:.2f}")
    return orden

def generar_archivo(ordenes):
    num = int(input("Ingrese el número de la orden a generar archivo: "))
    for orden in ordenes:
        if orden.numero == num:
            nombre_archivo = f"OrdenCompra_{num}.txt"
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(str(orden))
            print(f"\nArchivo '{nombre_archivo}' generado correctamente.")
            return
    print("\nNo se encontró la orden con ese número.")

def main():
    ordenes = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").lower()
        if opcion == "a":
            ver_ordenes(ordenes)
        elif opcion == "b":
            nueva = cargar_orden()
            ordenes.append(nueva)
        elif opcion == "c":
            generar_archivo(ordenes)
        elif opcion == "d":
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

