#!/usr/bin/python3


class Dispositivo_Entrada:
    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    def __str__(self):
        return f"Dispositivo de entrada: Tipo entrada: {self._tipo_entrada}, Marca: {self._marca}"

    @property
    def tipo_entrada(self):
        return self._tipo_entrada

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca


# Prueba de la clase actual
if __name__ == '__main__':
    dispositivo1 = Dispositivo_Entrada("USB", "ASUR")
    print(dispositivo1)
    print(dispositivo1.tipo_entrada)
    print(dispositivo1.marca)

    dispositivo2 = Dispositivo_Entrada("Cable", "DELL")
    print(dispositivo2)
    print(dispositivo2.tipo_entrada)
    print(dispositivo2.marca)