#!/usr/bin/python3
from poo.diseño_de_clase.Orden import Orden
from poo.diseño_de_clase.Producto import Producto

producto1 = Producto("libro", 10.00)
producto2 = Producto("ropa", 90.00)
producto3 = Producto("ron", 20.00)
producto4 = Producto("cerveza", 11.00)


productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f"Total de la orden1 ${orden1.calcular_total()} \n")
orden2 = Orden(productos2)
print(orden2)
print(f"Total de la orden 2 ${orden2.calcular_total()}")
