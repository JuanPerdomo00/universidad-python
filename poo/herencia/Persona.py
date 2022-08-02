#!/usr/bin/python3

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self.edad = edad

    def __str__(self):
        return f"Persona: {self._nombre} Edad: {self._edad}"


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleado: {super().__str__()} sueldo: {self.sueldo}"


empleado1 = Empleado("antonio", 20, 5000)
