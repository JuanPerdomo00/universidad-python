#!/usr/bin/python3

archivo = None

try:
    archivo = open("prueba.txt", "r", encoding="utf8")
    # print(archivo.read())

    # leer algunos caracteres
    # print(archivo.read(10))

    # leer lineas completas
    # print(archivo.readline())
    # print(archivo.readline())
except Exception as e:
    print("Error: ", e)

finally:
    archivo.close()
    print("Archivo cerrado")
