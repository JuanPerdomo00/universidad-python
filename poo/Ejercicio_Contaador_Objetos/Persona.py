#!/usr/bin/python3


class Persona:
    contador_persona = 0

    @classmethod
    def __generar__siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        self.id_persona = Persona.__generar__siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.id_persona} {self.nombre} {self.edad}"


persona1 = Persona("Juan", 40)
print(persona1)
persona2 = Persona("Karl", 20)
print(persona2)
persona3 = Persona("edgar", 22)
print(persona3)
print(f"Valor Contador Persona: {Persona.contador_persona}")
