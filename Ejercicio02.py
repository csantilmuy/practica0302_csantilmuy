# Añadir una clase Pedido que tiene como atributos:
#    - lista de productos
#    - lista de cantidades
# Añade las siguiente funcionalidad:
#    - total_pedido: muestra el precio final del pedido
#    - mostrar_productos: muestra los productos del pedido
class Pedido:
    def __init__(self):
        self.productos = []
        self.cantidades = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append(producto)
        self.cantidades.append(cantidad)

    def total_pedido(self):
        total = 0
        for producto, cantidad in zip(self.productos, self.cantidades):
            total += producto.calcular_total(cantidad)
        return total

    def mostrar_productos(self):
        for producto, cantidad in zip(self.productos, self.cantidades):
            print(f"Producto: {producto.get_nombre()}, Cantidad: {cantidad}, Precio unitario: {producto.get_precio()}")


class Producto:
    def __init__(self, codigo, nombre, precio):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def set_codigo(self, codigo):
        self._codigo = codigo

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_precio(self, precio):
        self._precio = precio

    def calcular_total(self, unidades):
        return self._precio * unidades


if __name__ == "__main__":
    camiseta = Producto(1, "Camiseta", 24)
    calcetines = Producto(2, "Calcetines", 3)

    pedido = Pedido()
    pedido.agregar_producto(camiseta, 3)
    pedido.agregar_producto(calcetines, 2)

    print("Productos en el pedido:")
    pedido.mostrar_productos()

    total = pedido.total_pedido()
    print(f"Precio total del pedido: {total}")