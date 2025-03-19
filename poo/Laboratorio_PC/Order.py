#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Order:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Order.contador_ordenes += 1
        self._id_ordenes = Order.contador_ordenes
        self._computadoras = list(computadoras)

    @property
    def id_ordenes(self):
        return self._id_ordenes

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for computadora in self._computadoras:
            computadoras_str += str(computadora.__str__()) + "\n"
        return f"""
        Orden {self._id_ordenes}
        {computadoras_str}
        """


# prueba
if __name__ == "__main__":
    pass
