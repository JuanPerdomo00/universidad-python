#!/usr/bin/python3


def listar_terminos(**kwargs):
    print(kwargs)
    for i, z in kwargs.items():
        print(f"Key: {i}, Value: {z}")


listar_terminos(astronomia="Jose Maza", fisica='Juan Perdomo', quimica='Marie curie', filosofia="friedrich", phicologia="Sigmund Freud")

