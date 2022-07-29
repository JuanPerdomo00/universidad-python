#!/usr/bin/python3


def retroceder(num):
    if num < 0:
        print("Valor no correcto")
    elif num == 0:
        return 0
    else:
        print(num) if num >= 1 else None
        return retroceder(num - 1)


n = int(input("Ingrese un numero: "))
retroceder(n)
