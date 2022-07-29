#!/usr/bin/python3

def main():
    edad = int(input("Ingrese su edad: "))
    if edad <= 0:
        print(f"{edad} es una edad negativa no permitido, por favor intente nuevamente")

    if 20 <= edad < 30:
        print(f"{edad} Esta en el rango de edad de jovensitos")
    else:
        print(f"{edad} edad fuera de rango")


if __name__ == "__main__":
    main()
