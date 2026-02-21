
# modelos/producto.py

# Clase base para productos de la tienda amazónica

# constructor, getters, setters, __str__ para representar el producto como string
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id  # ID único
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    # Método para representar el producto como string (útil para imprimir)
    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio:.2f}"