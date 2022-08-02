#!/usr/bin/python3
# ABC = Abstract Base Class

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Error valor no apto de ancho: {self.ancho}")
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Error valor no apto de alto: {self.alto}")

    def __str__(self):
        return f"Figura Geometrica: Alto {self._alto} Ancho: {self._ancho}"

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erroneo ancho: {ancho}")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"Valor erroneo alto: {alto}")

    @abstractmethod
    def calcular_area(self):
        pass
