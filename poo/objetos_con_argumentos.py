#!/usr/bin/python3
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalles(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")


persona1 = Persona("antonio", "Perdomo", 10)
persona2 = Persona("Jake", "Perez", 20)

# Modificar atributos de un objeto
persona1.nombre = "friedrich"
persona1.apellido = "lozano"
persona1.edad = 20

persona2.nombre = "paola"
persona2.apellido = "gomez"
persona2.edad = 90

persona1.mostrar_detalles()
persona2.mostrar_detalles()


