#!/usr/bin/python3

class Veiculo:
    def __init__(self, color: str, ruedas: int):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f"Color: {self._color}, Ruedas: {self._ruedas}"


class Coche(Veiculo):
    def __init__(self, color, ruedas, velocidad: int):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self):
        return f"Coche: {super().__str__()}, Velocidad: {self._velocidad} K/h"


class Bicicleta(Veiculo):
    def __init__(self, color, ruedas, tipo: str):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f"Bicicleta: {super().__str__()}, El tipo es: {self._tipo}"


