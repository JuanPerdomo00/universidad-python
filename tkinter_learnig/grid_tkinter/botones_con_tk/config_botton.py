#!/usr/bin/python3

import tkinter as tk
from tkinter import Tk, ttk


windows = Tk()

windows.title("Gird tkiner")
windows.geometry("600x400")
# windows.iconbitmap("../icono.ico")

# Configurar el grid
windows.rowconfigure(0, weight=1)
windows.rowconfigure(1, weight=10)
windows.columnconfigure(0, weight=1)
windows.columnconfigure(1, weight=5)
windows.columnconfigure(1, weight=1)
windows.columnconfigure(1, weight=5)


# Metodos de eventos
def a_event():
    btn1.config(text="Boton 1 presionado")


def b_event():
    btn2.config(text="Boton 2 presionado")


def c_event():
    btn4.config(text="Boton 4 presionado", fg="green", relief=tk.GROOVE, bg="red")


# definimos dos botones
btn1 = ttk.Button(windows, text="Boton 1", command=a_event)
btn1.grid(row=0, column=0, sticky="NSWE")

btn2 = ttk.Button(windows, text="Boton 2", command=b_event)
btn2.grid(row=1, column=0, sticky="NSWE")

btn3 = ttk.Button(windows, text="Boton 3")
btn3.grid(row=0, column=1, sticky="NSWE")

btn4 = tk.Button(windows, text="Boton 4", command=c_event)
btn4.grid(row=1, column=1, sticky="NSWE")


windows.mainloop()
