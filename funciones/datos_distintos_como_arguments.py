#!/usr/bin/python3


def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)


nombre_list = ["juan", "victor", "soledad", "socrates"]

desplegar_nombres(nombre_list)
desplegar_nombres("freud")
desplegar_nombres((1, 3))
desplegar_nombres([10, 11])
