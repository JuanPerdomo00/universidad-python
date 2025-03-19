#!/usr/bin/python3
# -*- coding: utf-8 -*-
# github.com/JuanPerdomo00


from Peliculas.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas
from Color_ascci_cli.Color import Color as c
import platform as pl
import os


# import time


def clear():
    "clear" if pl.system() == "Windows" else os.system("clear")


# def relog():
# time.sleep(2)
# print("Regresando al menu en seg...")
# seg_i = 0
# seg_f = 5
# while seg_i < seg_f:
# seg_i += 1
# time.sleep(1)
# return seg_i


def menu():
    print(f"{c.RED}Programa de peliculas{c.OFF}".center(50, "-"), "\n")
    print(f"{c.GREEN} 1. Agregar pelicula {c.OFF}")
    print(f"{c.GREEN} 2. Listar peliculas {c.OFF}")
    print(f"{c.GREEN} 3. Eliminar peliculas {c.OFF}")
    print(f"{c.GREEN} 4. Salir{c.OFF}")
    print(f"{c.CYAN}By Jakepy{c.OFF}".center(50, "-"))


def main():
    clear()
    menu()
    opcion = None
    try:
        while opcion != 4:
            opcion = int(input("[*] Ingrese una opcion: ".title()))
            if opcion == 1:
                clear()
                menu()
                nombre = input("Ingrese el nombre de la pelicula: ")
                pelicula = Pelicula(nombre)
                catalogo = CatalogoPeliculas("peliculas.txt")
                catalogo.agregar_pelicula(pelicula)

            elif opcion == 2:
                clear()
                menu()
                catalogo = CatalogoPeliculas("peliculas.txt")
                catalogo.listar_peliculas()

            elif opcion == 3:
                clear()
                menu()
                catalogo = CatalogoPeliculas("peliculas.txt")
                catalogo.eliminar_peliculas()
            else:
                print(f"{c.RED}[!] Opcion incorrecta {c.OFF}")
    except KeyboardInterrupt as e:
        print(f"{c.MAGENTA}Saliendo...\n{c.OFF}")
        os.system(
            "echo gracias por usar el programa. by Jakepy && cowsay -f tux 'Tu seras un grande' "
        )
        os.system("exit 1")
    except ValueError as e:
        clear()
        menu()
        print(
            f"{c.RED} Error al ingresar la opcion: {e} Posiblemente la causa fue un espacio{c.OFF} "
        )


if __name__ == "__main__":
    main()
