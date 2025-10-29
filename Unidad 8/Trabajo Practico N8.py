#ejercicio1
with open("productos.txt", "w") as productos:
    productos.write("Manzana,1600,5\n")
    productos.write("Galletas,2000,10\n")
    productos.write("Banana,1000,7\n") 


#ejercicio2
with open("productos.txt", "r") as productos:
    for linea in productos:
        datos = linea.strip().split(",")
        producto = datos[0]
        precio= datos[1]
        cantidad= datos[2]
        print(f"Producto: {producto} | Precio: {precio} | Cantidad: {cantidad}")


#ejercicio3
print("-----Productos-----")
print(f"Producto: {producto} | Precio: {precio} | Cantidad: {cantidad}")
nuevo_producto= input("Ingrese el nombre del nuevo producto: ")
precio_producto= input("Ingrese el precio del nuevo producto: ")
cantidad_producto= input("Ingrese la cantidad del nuevo producto: ")

with open("productos.txt","a") as productos:
    productos.write(f"{nuevo_producto},{precio_producto},{cantidad_producto}\n")

#mostrar toda la lista completa de productos
with open("productos.txt", "r") as productos:
    for linea in productos:
        datos = linea.strip().split(",")
        producto = datos[0]
        precio= datos[1]
        cantidad= datos[2]
        print(f"Producto: {producto} | Precio: {precio} | Cantidad: {cantidad}")


#ejercicio4
productos_lista= []
with open("productos.txt", "r") as productos:
    for linea in productos:
        datos = linea.strip().split(",")
        nombre = datos[0]
        precio= datos[1]
        cantidad= datos[2]
        producto_dict= {"nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad}
        productos_lista.append(producto_dict)
print(productos_lista)


#ejercicio5
nombre_producto= input("Ingrese el nombre del producto a buscar: ").lower()
encontrado= False

for producto in productos_lista:
    if producto["nombre"].lower() == nombre_producto:
        print(f"Producto: {producto} | Precio: {precio} | Cantidad: {cantidad}")
        encontrado= True
        break
if not encontrado:
    print(f"El producto {nombre_producto} no se encuentra en la lista.")



#ejercicio6
with open("productos.txt","w") as productos:
    for producto in productos_lista:
        productos.write(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}\n")

print("Archivo productos.txt actualizada")
