#!/usr/bin/python3

from excepciones.NumerosIgualesException import NumerosIgualesException

resultado = None

try:
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    resultado = a / b
    if a == b:
        raise NumerosIgualesException("Numeros iguales")
except ValueError as e:
    print(f"ValueError: {e}", type(e))
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}", type(e))
except TypeError as e:
    print(f"TypeError: {e}", type(e))
except Exception as e:
    print(f"Exception Error: {e}", type(e))
else:
    print("NO se arrojo ninguna exception")

finally:
    for i in range(1, 10):
        print(f"{i} siempre me ejecuto")

print(f"El resultado es: {resultado}")
print("Continuamos con el programa...")
