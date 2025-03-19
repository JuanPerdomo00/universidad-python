#!/usr/bin/python3


class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print("Obtenemos el recurso".center(50, "-"))
        self.nombre = open(self.nombre, "r", encoding="utf-8")
        return self.nombre

    def __exit__(self, tipo, valor, traza_del_error):
        print("Cerramos el recurso".center(50, "-"))
        if self.nombre:
            self.nombre.close()
