#!/usr/bin/python3

from tkinter import Tk, ttk


windows = Tk()

windows.title("Gird tkiner")
windows.geometry("600x400")
# windows.iconbitmap("../icono.ico")


# Metodos de eventos
def a_event():
    btn1.config(text="Boton 1 presionado")


def b_event():
    btn2.config(text="Boton 2 presionado")


# definimos dos botones
btn1 = ttk.Button(windows, text="Boton 1", command=a_event)
btn1.grid(row=0, column=0)

btn2 = ttk.Button(windows, text="Boton 2", command=b_event)
btn2.grid(row=1, column=1)


windows.mainloop()
