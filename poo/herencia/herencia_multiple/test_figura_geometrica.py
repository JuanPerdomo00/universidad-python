#!/usr/bin/python3

from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
# from herencia_multiple import FiguraGeometrica

# No se puede insxtanciar una clase abstracta
# figura = FiguraGeometrica(20, 30)
# figura.calcular_area()

print("Creacion de objeto cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(11, "rojo")
print(cuadrado1.calcular_area())

print("Creacion de objeto rectangulo".center(50, "-"))
rectangulo1 = Rectangulo(220, 220, "verde")
print(rectangulo1.calcular_area())
print(rectangulo1)
