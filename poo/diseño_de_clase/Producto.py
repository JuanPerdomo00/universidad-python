#!/usr/bin/python3


class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def id(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID Producto: {self._id_producto},  Nombre: {self._nombre}, Precio: {self._precio}"


if __name__ == "__main__":
    preducto1 = Producto("libro", 10.00)
    preducto2 = Producto("ropa", 90.00)
    print(preducto1)
    print(preducto2)
