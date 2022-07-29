#!/usr/bin/python3


def multi(*num: int):
    lista = [i for i in num]
    resultado = 1

    for numeros in lista:
        resultado *= numeros

    return resultado


print(multi(5, 5, 2))
