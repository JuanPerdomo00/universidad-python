#!/usr/bin/python3
# -*- coding: utf-8 -*-
# github.com/JuanPerdomo00

class Pelicula:

    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

