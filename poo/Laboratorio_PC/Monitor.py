#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitores += 1
        self._id_monitores = Monitor.contador_monitores
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f"ID Monitor: {self._id_monitores}, Marca: {self._marca}, Tamaño: {self._tamaño}"

    @property
    def marca(self):
        return self.marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño


# Prueba de la clase actual
if __name__ == "__main__":
    monitor1 = Monitor("hp", "100 pulgadas")
    print(monitor1)
    monitor2 = Monitor("dell", "120 pulgadas")
    print(monitor2)
