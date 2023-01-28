#!/usr/bin/python3

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 *  6
# 5! = 5 * 24
# 5! = 120


def factorial(num: int) -> int:
    if num == 1:
        return 1

    return num * factorial(num - 1)


numero: int = int(input("Ingrese el numero a hayar el factorial: "))

print("El factorial de %d es: " % factorial(numero))
