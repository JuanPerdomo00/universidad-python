#!/usr/bin/python3

def mi_funcion():
    print("Saludos desde esta funcion")

    return 0


#  Funcion con parametros
# ! Parametros son las variables que recivira nuestra funcion
# ! Argumento donde vamos enviar los valores de las variables 

def saludar(nombre: str, apellido: str) -> str:  # ? Parametros
    return f"Hola como estas 'Dr 👨‍🔬 {nombre.capitalize()} {apellido.capitalize()}'"


print(saludar("juan", "perdomo"), end="\n")  # ? Argumentos
print(saludar("max", "planck"), end="\n")
