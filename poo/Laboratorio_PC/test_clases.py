#!/usr/bin/python3
from poo.Laboratorio_PC.Computadora import Computadora
from poo.Laboratorio_PC.Monitor import Monitor
from poo.Laboratorio_PC.Order import Order
from poo.Laboratorio_PC.Raton import Raton
from poo.Laboratorio_PC.Teclado import Teclado


print("Tienda de computadoras".center(50, "-"))

monitor1 = Monitor("hp", "100 pulgadas")
teclado1 = Teclado("hp", "usb")
raton1 = Raton("hp", "usb")
computadora1 = Computadora('carpy', monitor1, teclado1, raton1)
print(computadora1)

monitor2 = Monitor("dell", "120 pulgadas")
teclado2 = Teclado("dell", "ps2")
raton2 = Raton("dell", "ps2")
computadora2 = Computadora('molly', monitor2, teclado2, raton2)
print(computadora2)

monitor3 = Monitor("acer", "150 pulgadas")
teclado3 = Teclado("gamer", "usb")
raton3 = Raton("acer", "cable")
computadora3 = Computadora('acer', monitor3, teclado3, raton3)
print(computadora3)

computadoras1 = [computadora1, computadora2]
orden1 = Order(computadoras1)
print(orden1)

computadoras2 = [computadora3]
orden2 = Order(computadoras2)
print(orden2)

orden1.agregar_computadora(computadora3)
print(orden1)
