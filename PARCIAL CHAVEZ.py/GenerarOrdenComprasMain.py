from Producto import Producto
from DetalleOrdenCompra import DetalleOrdenCompra
from OrdenCompra import OrdenCompra

def mostrar_menu():
    print("MENÚ ORDENES DE COMPRA")
    print("a) Ver Órdenes de Compra Cargadas")
    print("b) Cargar 1 o más Órdenes de Compra")
    print("c) Generar Archivo de Orden de Compra por número")
    print("d) Salir")

def ver_ordenes(ordenes):
    if orden in ordenes:
        for orden in ordenes:
            print(orden)

def main():
    ordenes = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").lower()
        if opcion == "a":
            ver_ordenes(ordenes)
        elif opcion == "d":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()












