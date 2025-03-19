#!/usr/bin/python3


class Rectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def area_rectangulo(self):
        area = self.base * self.altura
        print(f"El area de el rectangulo es: {area}")


def main():
    print("Hallar el area de un rectangulo")
    b = int(input("Ingrese la base de el rectangulo: "))
    a = int(input("Ingrese la altura de el rectangulo: "))
    rect = Rectangulo(b, a)

    rect.area_rectangulo()


if __name__ == "__main__":
    main()
