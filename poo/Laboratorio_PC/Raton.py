#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Dispositivo_Entrada import Dispositivo_Entrada


class Raton(Dispositivo_Entrada):
    contador_ratones = 0

    # @classmethod
    # def contador(cls):
    #   cls.contador_ratones += 1

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Raton.contador_ratones += 1
        self._id_ratones = Raton.contador_ratones

    def __str__(self):
        return f"ID Raton: {self._id_ratones}, Tipo entrada: {self.tipo_entrada}, Marca: {self.marca}"


# Prueba de la clase actual
if __name__ == '__main__':
    raton1 = Raton("USB", "Dell")
    print(raton1)
    raton2 = Raton("cable", "acer")
    print(raton2)
