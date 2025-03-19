#!/usr/bin/python3


def calcular_impuesto(pago_sin, impuesto):
    return pago_sin + pago_sin * (impuesto / 100)


pago_sin_impuesto = int(input("Ingrese el pago sin impuesto: "))
impuestos = int(input("Ingrese el impuesto: "))

if __name__ == "__main__":
    calculo = calcular_impuesto(pago_sin_impuesto, impuestos)
    print(f"Pago con impuesto es: {calculo}")
