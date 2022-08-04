#!/usr/bin/python3
from poo.polimorfismo.polimorfismo import Empleado
from poo.polimorfismo.Gerente import Gerente


def imprimir_detalle(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalle())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Jakepy", -2000)
imprimir_detalle(empleado)

gerente = Gerente("abc", 3000, "Ciencias fisica")
imprimir_detalle(gerente)
