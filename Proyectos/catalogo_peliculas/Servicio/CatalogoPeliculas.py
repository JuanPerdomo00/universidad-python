#!/usr/bin/python3
# -*- coding: utf-8 -*-
# github.com/JuanPerdomo00


import os


class CatalogoPeliculas:
    def __init__(self, archivo):
        self.ruta = archivo

    def agregar_pelicula(self, pelicula):
        try:
            with open(self.ruta, "a") as archivo:
                archivo.write(f"{pelicula.nombre}\n")
                print(f"La pelicula {pelicula.nombre} fue agregada correctamente \n")

        except Exception as e:
            print("Error: ", e)

    def listar_peliculas(self):
        try:
            i = 0
            with open(self.ruta, "r", encoding="utf8") as archivo:
                print("Lista de Peliculas".center(50, "-"))
                for lista in archivo.readlines():
                    i += 1
                    print(f"ID: [{i}] Pelicula: {lista}")
        except FileNotFoundError as e:
            print(f"Error al listar, El archivo {self.ruta} no existe", e)

    def eliminar_peliculas(self):
        ruta = self.ruta
        try:
            if os.path.exists(ruta):
                os.remove(ruta)
                print(f"El erchivo {ruta} fue eliminado correctamente en la ruta")
                os.system(f"echo $('pwd')/{ruta}")
            else:
                print(f"El archivo {ruta} no existe posiblemente ya fue eliminado")
        except FileNotFoundError as e:
            print("Error: ", e)
