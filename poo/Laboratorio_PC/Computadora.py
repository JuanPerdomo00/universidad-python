#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"""
        Computadora: 
        ID Computadora: {self._id_computadora}, 
        Nombre: {self._nombre}, 
        Monitor: {self._monitor}, 
        Teclado: {self._teclado}, 
        Raton: {self._raton} 
        """

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def id_computadora(self):
        return self._id_computadora


# Prueba de la clase actual
if __name__ == '__main__':
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
