from datetime import date
from DetalleOrdenCompra import DetalleOrdenCompra

class OrdenCompra:
    contador = 1

    def __init__(self):
        self.fecha = date.today()
        self.numero = OrdenCompra.contador
        self.lista_detalles = []
        self.total = 0.0
        OrdenCompra.contador += 1

    def agregar_detalle(self, detalle):
        self.lista_detalles.append(detalle)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(detalle.subtotal for detalle in self.lista_detalles)

    def __str__(self):
        detalles = "\n".join(str(d) for d in self.lista_detalles)
        return (f"Orden de Compra {self.numero}"
                f"Fecha: {self.fecha}"
                f"Detalles: {detalles}"
                f"Total: ${self.total:.2f}")