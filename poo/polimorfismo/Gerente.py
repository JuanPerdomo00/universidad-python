#!/usr/bin/python3
from Polimorfismo import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f"Generate: {self.departamento} {super().__str__()}"


