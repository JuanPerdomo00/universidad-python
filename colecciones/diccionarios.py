#!/usr/bin/python3

# Esta compuesto por una (llave, valor)

cientificos = {
    "Fisica": "Max Plank",
    "Quimica": "Marie Curine",
    "Atronomia": "Jose Maza",
    "Biologia": "Charles Darwin",
    "computacion": "Alan Turing",
}

print(cientificos)

# Conocer la cantidad de elementos
print(len(cientificos))

# acceder a un elemento (key)
print(cientificos["Fisica"])

# otra forma de recuperar un elemento
print(cientificos.get("Quimica"))

# modificar elementos de un diccionario

cientificos["Fisica"] = "Juan Perdomo".upper()
print(cientificos)

# recorrer los elementos de un diccionario
for key, value in cientificos.items():
    print(key, "->", value)

# comprobar si existe un elemento
print("Fisica" in cientificos)

# agregar un elemento
cientificos["Filosofo"] = "Friedric Nietzsche"
print(cientificos.keys())

# remover un elemento
cientificos.pop("computacion")
print(cientificos)

# limpiar
cientificos.clear()

# eliminar el diccionario
del cientificos
print(cientificos)
