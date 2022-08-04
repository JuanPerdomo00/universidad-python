#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Dispositivo_Entrada import Dispositivo_Entrada

class Teclado(Dispositivo_Entrada):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Teclado.contador_teclados += 1
        self._id_teclados = Teclado.contador_teclados

    def __str__(self):
        return f"ID Teclado: {self._id_teclados}, Tipo de entrada: {self.tipo_entrada} Marca: {self.marca}"


# Prueba de la clase actual
if __name__ == '__main__':
    teclado1 = Teclado("USB", "DELL")
    teclado2 = Teclado("Cameron", "COMP")
    print(teclado1, "\n", teclado2)