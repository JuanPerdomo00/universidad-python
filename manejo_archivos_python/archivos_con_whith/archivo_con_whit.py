#!/usr/bin/python3

# with open("../prueba.txt", "r", encoding="utf-8") as archivo:
from ManejoArchivos import ManejoArchivos

with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.readlines())
