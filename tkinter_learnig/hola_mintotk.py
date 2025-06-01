#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

# Creamos un objeto usando la clase tk
ventana = tk.Tk()

# Modificar el tamanio ventana (pixeles)

ventana.geometry("600x400")

# cambiar nombre de la ventana
ventana.title("Nueva ventana")

# configuramos icono
ventana.iconbitmap()


# Creamos un metodo evento_click
def evento_click():
    boton1.config(text="Boton clicked")
    print("Ejecutando del evento_click")
    # Creamos un nuevo boton y lo mostramos
    boton2 = ttk.Button(ventana, text="Nuevo boton")
    boton2.pack()


# Crear un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text="Dar click", command=evento_click)

# utilizar el pack layout manager, para mostrar el boton
boton1.pack()

# Iniciamos la ventana (al final)
ventana.mainloop()
