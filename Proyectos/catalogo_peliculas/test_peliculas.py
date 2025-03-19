#!/usr/bin/python3
# -*- coding: utf-8 -*-
# github.com/JuanPerdomo00


from Peliculas.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas

# agregar
nombre = input("Ingrese el nombre de la pelicula: ")
pelicula = Pelicula(nombre)
catalogo = CatalogoPeliculas("peliculas.txt")
catalogo.agregar_pelicula(pelicula)

# listar
catalogo = CatalogoPeliculas("peliculas.txt")
catalogo.listar_peliculas()

# eliminar
catalogo = CatalogoPeliculas("peliculas.txt")
catalogo.eliminar_peliculas()
