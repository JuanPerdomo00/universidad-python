#!/usr/bin/python3


class Perritos:
    def __init__(self, nombre, raza, edad, sexo):
        self._nombre = nombre
        self._raza = raza
        self._edad = edad
        self._sexo = sexo

    def mostrar(self):
        print(f"""
        El perro se llama: {self._nombre}
        La raza es: {self._raza}
        La Edad de el perro es: {self._edad} años
        El sexo de el perro es: {self._sexo} 
    """)


primer_perrito = Perritos("toby", "pincher", 5, "macho")
primer_perrito._nombre = "tovias"
primer_perrito.mostrar()
