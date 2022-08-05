#!/usr/bin/python3

# primero hay que abrir un archivo
# para abrir un archivo se utiliza la funcion open
# la funcion open recibe dos parametros
# el primero es el nombre del archivo
# el segundo es el modo de apertura
# el modo de apertura es un string
# los modos de apertura son:
# r: lectura
# w: escritura
# a: añadir
# r+: lectura y escritura
# w+: lectura y escritura
# a+: lectura y escritura
# b: modo binario
# t: modo texto
# el modo de apertura por defecto es r
# si no se especifica el modo de apertura se utiliza el modo de apertura por defecto

archivo = None

try:
    archivo = open("prueba.txt", "w", encoding="utf-8")
    archivo.write("Hola mundo desde python al archivo \n")
    archivo.write("Adios")
except Exception as e:
    print("Error: ", e)
finally:
    archivo.close()
    print("Archivo cerrado")
