# Crear una Clase Producto con los siguientes atributos:
# - código
# - nombre
# - precio 
# Crea su constructor, getter y setter y una función llamada calcular_total,
# donde le pasaremos unas unidades y nos debe calcular el precio final.
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

producto = Producto(1, "Aguacate", 0.9)
print(f"Nombre: {producto.get_nombre()}, Código: {producto.get_codigo()}, Precio unitario: {producto.get_precio()}")

unidades = 10
precio_total = producto.calcular_total(unidades)
print(f"Precio total para {unidades} unidades: {precio_total}")