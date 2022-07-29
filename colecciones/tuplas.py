#!/usr/bin/python3

# Definir una tupla
frutas = ("Naranja", "Banano", "Manzana")

# indice     0          1          2
print(frutas)
# se maneja el mismo orden de indice como las listas, salvo que son inmutables


# Saber el largo de una tupla
print(len(frutas))

# acceder a un elemento
print(frutas[2])

# Navegacion inversa
print(frutas[-1])

# Acceder a un rango
print(frutas[0:2])  # Sin incluir un indice


# recorrer los elementos de lo tupla

for fruta in frutas:
    print(fruta, end=" ")

# cambiar el valor de una tupla
lista_frutas = list(frutas)
lista_frutas[0] = "Fresa"
frutas = tuple(lista_frutas)
print("\n", frutas)

# Eliminar tupla
del frutas
print(frutas)