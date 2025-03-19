#!/usr/bin/python3


class Persona:
    """
    Puede tener atributos y metodos
    """

    # metodo inicializador
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalles(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

    def mostrar_args_kwargs(self):
        print(f"Args: {self.valores}")
        print(f"Kwargs: {self.terminos}")


persona1 = Persona(
    "Juan", "Perdomo", 19, 3132324, 1, 2, 3, 4, phicologia="Sigmund freud"
)

persona1.mostrar_detalles()
persona1.mostrar_args_kwargs()
