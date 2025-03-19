#!/usr/bin/python3


def celsius_fahrenheit(c):
    """
    formula = f = (1.8 * c) + 32
    :param c:
    :return f:
    """

    return (1.8 * c) + 32


def fahrenheit_celsius(f):
    """
    :param f:
    :return f - 32 / 1.8:
    """

    return (f - 32) / 1.8


def main():
    print("*" * 50)
    print("\t\t\tConvertidor de Temperature")
    print("*" * 50)

    print(
        """
    [*] 1 -> Convertir de celsius a fahrenheit
    [*] 2 -> Convertir de fahrenheit a celsius
    [*] 3 -> Salir
    """,
        end="\n",
    )

    opcion = int(input("Ingresa una opcion: "))

    while opcion != 3:
        if opcion == 1:
            celsius = int(input("Ingrese los grados celsius: "))
            print(f"Los grados Fahrenheit son: {celsius_fahrenheit(celsius)}")
            break
        elif opcion == 2:
            fahrenheit = int(input("Ingrese los grados fahrenheit: "))
            print(f"Los grados Fahrenheit son: {fahrenheit_celsius(fahrenheit)}")
            break
        else:
            print("Opcion no valida")
            break


if __name__ == "__main__":
    main()
