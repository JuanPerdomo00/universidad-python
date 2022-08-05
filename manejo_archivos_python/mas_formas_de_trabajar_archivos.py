#!/usr/bin/python3

archivo = open("prueba.txt", "r", encoding="utf-8")


# leer el archivo
# iterar sobre el archivo
# for linea in archivo:
    # print(linea)
    # pass

# leer linas
# print(archivo.readlines())

# acceder a una linea de la lista
# print(archivo.readlines()[0])

# crear una copia del archivo original
archivo_copia  = open("copia.txt", "a", encoding="utf-8")
archivo_copia.write(archivo.read())

archivo.close()
archivo_copia.close()
print("Terminado el proceso de copiado y creado ded archivo")
