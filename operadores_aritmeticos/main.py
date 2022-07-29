#!/usr/bin/python3

def suma(x, y):
    return x + y


def restar(x, y):
    return x - y


def multiplicacion(x, y):
    return x * y


def divicion(x, y):
    return x / y


def divicion_entera(x, y):
    return x // y


def exponenciacion(x, y):
    return x ** y


def modulo(x, y):
    return x % y


def main():
    print("Que deseas hacer sumar[1] restar[2] multiplicar[3]")
    print("dividir[4] dividir entero[5] exponenciar[6] modulo[7]")

    opcion = int(input("Ingresa la opcion: "))
    a = int(input("Ingresa un numero: "))
    b = int(input("Ingresa un numero: "))

    if opcion == 1:
        suma(a, b)
        print(f"La suma de {a} y {b}  es: {suma(a, b)}")
    elif opcion == 2:
        print(f"La resta de {a} y {b} es: {restar(a, b)}")
    elif opcion == 3:
        print(f"La multiplicacion de {a} y {b} es: {multiplicacion(a, b)}")
    elif opcion == 4:
        print(f"La de {a} entre {b} es: {divicion(a, b)}")
    elif opcion == 5:
        print(f"La divicion entere entre {a} y {b} es: {divicion_entera(a, b)}")
    elif opcion == 6:
        print(f"La potencia de la base {a} y el exponente {b} es: {exponenciacion(a, b)}")
    elif opcion == 7:
        print(f"El modulo de {a} entre {b} es: {modulo(a, b)}")

    else:
        print("Error opcion no encontrada")
        nombre = input("Porfavor deje su nombre para una futura operacion: ").capitalize()
        print(f"Gracias por usar el programa {nombre}")
        main()


if __name__ == "__main__":
    main()
