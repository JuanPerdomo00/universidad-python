#!/usr/bin/python3

"""
Crear una funcion para sumar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la funcion
y regresar como resultado la suma de todos los valores pasados como argumentos
"""


def sumar(*num: int):
    lista = list(num)
    suma = 0
    lista_suma = []

    for i in lista:
        lista_suma.append(i)

    for numeros in lista_suma:
        suma += numeros

    return suma


print(sumar(10, 20, 30, 40, 50))
