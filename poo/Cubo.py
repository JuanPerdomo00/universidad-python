#!/usr/bin/python3

class Cubo:
    def __init__(self, anchoX, profundoZ, altoY):
        self.anchoX = anchoX
        self.profundoZ = profundoZ
        self.altoY = altoY

    def calcular_volumen(self):
        vol = self.anchoX * self.profundoZ * self.altoY
        print(f"El volumen de el cubo es: {vol}m^3")
        return vol


def main():
    print("Calcula el volumen de un cubo")
    x = int(input("Ingresa el ancho del cubo: "))
    z = int(input("Ingresa la profundidad de el cubo: "))
    y = int(input("Ingresa el alto de el cubo: "))

    cubo = Cubo(x, z, y)

    cubo.calcular_volumen()


if __name__ == '__main__':
    main()
