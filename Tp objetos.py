class componenteCPU:
    listacomponentes= []
    def __init__(self,componente,marca,cantidad,precio):
        self.componente = str(componente)
        self.marca = str(marca)
        self.cantidad = int(cantidad)
        self.precio = float(precio)
        componenteCPU.listacomponentes.append(self)
    def __str__(self):
        return f"{self.componente} ({self.marca}) - Cantidad: {self.cantidad}, Precio: ${self.precio}"

class computadora: 
    def __init__(self,marca,modelo,listacomponentes):
        self.marca= str(marca)
        self.modelo= str(modelo)
        self.listacomponentes= listacomponentes

    def calcular_costo(self):
        total= 0
        for c in self.listacomponentes:
            total += c.cantidad * c.precio
        return total
        
    def calcular_precio_venta(self):
        costo = self.calcular_costo()
        if costo < 50000:
            return costo + (costo * 0.40)
        else:
            return costo + (costo * 0.30)



    def mostrar_informacion(self):
        print("------ COMPUTADORA ------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("Componentes:")
        for c in self.listacomponentes:
            print("  -", c)

        costo = self.calcular_costo()
        precio_venta = self.calcular_precio_venta()

        print(f" Costo total: ${costo}")
        print(f"Precio de venta sugerido: ${precio_venta}")

def cargar_componentes_desde_archivo():
    componentes = []
    try:
        with open("componentes.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                comp = datos[0]
                marca = datos[1]
                cant = int(datos[2])
                precio = float(datos[3])
                nuevo = componenteCPU(comp, marca, cant, precio)
                componentes.append(nuevo)
    except FileNotFoundError:
        print("Archivo de componentes no encontrado. Se creará uno nuevo.")
    return componentes        


class CostoComputadora:
    def main(self):
        while True:
            marca = input("Ingrese la marca de la computadora: ")
            modelo = input("Ingrese el modelo de la computadora: ")

            componentes = []
            n = input("Ingrese los componentes y escriba fin para terminar ")

            while True:
                comp = input("Nombre del componente: ")
                if comp.lower() == "fin":
                    break
                marca_comp = input("Marca del componente: ")
                try:
                   cant = int(input("Cantidad: "))
                   if cant < 0:
                          print("La cantidad no puede ser negativa. Intente nuevamente.")
                          continue
                   break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")
            while True:
                try:
                    precio = float(input("Precio unitario: "))
                    if precio < 0:
                        print("El precio no puede ser negativo. Intente nuevamente.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido para el precio.")

                nuevo = componenteCPU(comp, marca_comp, cant, precio)
                componentes.append(nuevo)

            pc = computadora(marca, modelo, componentes)
            pc.mostrar_informacion()

            continuar = input("¿Desea evaluar otra computadora? (SI/NO): ").upper()
            if continuar == "NO":
                print("Programa finalizado.")
                break


# Ejecutar el programa principal
if __name__ == "__main__":
    programa = CostoComputadora()
    programa.main()

