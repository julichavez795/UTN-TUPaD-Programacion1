from productos import Producto

class DetalleOrdenCompra:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = int(cantidad)
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        return self.producto.precio_compra * self.cantidad

    def __str__(self):
        return f"{self.producto.denominacion} x{self.cantidad} - Subtotal: ${self.subtotal:.2f}"
