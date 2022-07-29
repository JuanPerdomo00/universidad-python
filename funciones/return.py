#!/usr/bin/python3


def suma(a: int, b: int) -> int:
    return a + b


resultado = suma(10, 20)
print(f"La suma es: {resultado}")


# valores por default a los parametros de una funcion
def restar(a: int = 0, b: int = 2) -> int:
    return a - b


res = restar(1, 2)
print(f"La resta es: {res}")
