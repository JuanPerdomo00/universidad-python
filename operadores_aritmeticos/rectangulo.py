#!/usr/bin/python3
"""
NOTE: Ejercicio de area y perimetro de triangulo
"""


def area_perimetro(a: int, p: int):
    area = a * p
    perimetro = (a + p) * 2

    return area, perimetro


alto = int(input("Ingresa el alto de el rectangulo: "))
ancho = int(input("Ingresa el alto de el rectangulo: "))

print(f"Area: {area_perimetro(alto, ancho)}")
print(f"Perimetro: {area_perimetro(alto, ancho)}")
