#!/usr/bin/python3

from colorama import Fore


class Color:
    """
    Esta clase trae los colores desde colorama usando su propiedad Fore
    """
    off = Fore.RESET
    red = Fore.RED
    green = Fore.GREEN
    blue = Fore.BLUE
    yellow = Fore.YELLOW


class Clientes:
    """
    Esta clase se encarga de crear un objeto
    sus metodos son saludar, depedir y dar error
    """
    def __init__(self, nick: str):
        self.nick = nick or "anonymous"

    def saludar_cliente(self):
        print(f"{Color.green}Bienvenido {self.nick.capitalize()}{Color.off}")

    def despedir_cliente(self):
        print(f"Hasta luego Sr {self.nick.capitalize()}")

    def error_cliente(self):
        print(f"{Color.red}OPPs... Sr {self.nick.upper()} Opcion no valida{Color.off}")


class Aritmetica:
    """
    La clase aritmetica se encarga de crear los objetos
    y sus metodos son los que ayudaran hacer las operaciones
    """
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        resultado = self.n1 + self.n2
        print(f"La suma de {self.n1} y {self.n2}  es: {resultado}")

    def restar(self):
        resultado = self.n1 - self.n2
        print(f"La resta de {self.n1} y {self.n2} es: {resultado}")

    def multiplicar(self):
        resultado = self.n1 + self.n2
        print(f"El resultado de la multiplicacion de {self.n1} y {self.n2} es: {resultado}")

    def divicion(self):
        resultado = self.n1 / self.n2
        print(f"El resultado de la divicion de {self.n1} y {self.n2} es: {resultado:.2f}")


def banner():
    """
    Imprime un banner en la terminal
    :return: None
    """
    print(f"{Color.red}={Color.off}" * 50)
    print(f"{Color.green}Calculadora con programing orientate a objets{Color.off}")
    print(f"{Color.red}={Color.off}" * 50)


def menu():
    """
    Imprime el menu de opciones
    :return: None
    """

    print(f"""
{Color.yellow}Ingresa una opcion
[1] Sumar
[2] Restar
[3] Multiplicar
[4] Dividir
[5] Salir
{Color.off}""")


def main():
    banner()
    # Istanciamos desde la clase clientes y creamos un nuevo objeto cliente
    cliente = Clientes(input(f"{Color.blue}[*] Ingresa ti nick: {Color.off}"))
    cliente.saludar_cliente()

    menu()

    opcion = int(input(": "))

    while opcion != 5:
        if opcion == 1:
            a = int(input("Ingrese un numero: "))
            b = int(input("Ingrese otro numero: "))

            sumar = Aritmetica(a, b)
            sumar.suma()
            break
        elif opcion == 2:
            a = int(input("Ingrese un numero: "))
            b = int(input("Ingrese otro numero: "))

            restar = Aritmetica(a, b)
            restar.restar()
            break
        elif opcion == 3:
            a = int(input("Ingrese un numero: "))
            b = int(input("Ingrese otro numero: "))

            multiplicar = Aritmetica(a, b)
            multiplicar.multiplicar()
            break
        elif opcion == 4:
            a = int(input("Ingrese un numero: "))
            b = int(input("Ingrese otro numero: "))

            dividir = Aritmetica(a, b)
            dividir.divicion()
            break
        else:
            cliente.error_cliente()
            break
    else:
        print("Termino el programa")
        cliente.despedir_cliente()


if __name__ == '__main__':
    main()
