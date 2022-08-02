#!/usr/bin/python3

class Persona:
    """
    Metodos Get y Set

    Los metodos de tipo get nos van a permitir obtener los atributos de nuestra clase
    Los metodos de tipo set nos can a permitir modificar los atributos de nuestra clase

    Por cada uno de los atributos vamos a crear un metodo get y set respectivo

    Siempre que veamos atributos con _ o con __ son atributos encapsulados en nuestra clase
    """

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # Definimos un metodo get para recuperar el valor de el atributo de nombre de manera individual
    @property
    def nombre(self):
        return self._nombre

    # Modificar el atributo con set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self.edad = edad

    def mostrar(self):
        print(f"Persona {self._nombre} {self._apellido} {self._edad}")

    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido} {self._edad} fue eliminado")


if __name__ == '__main__':
    persona1 = Persona("jakepy", "perdomo", 20)
    persona1.nombre = "friedrich"
    print(persona1.nombre)
    persona1.mostrar()
