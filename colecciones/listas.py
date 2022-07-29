#!/usr/bin/python3

nombre = ["jake", "lili", "friederich", "antonio", "van goh"]
# indices   0       1          2           3           4
# inverso  -5       -4         -3          -2          -1

print("0", nombre[0], end=". \n")
print("1", nombre[1], end=". \n")
print("2", nombre[2], end=". \n")
print("3", nombre[3], end=". \n")
print("4", nombre[4], end=". \n")

print("\n")

print("-1", nombre[-1], end=". \n")
print("-2", nombre[-2], end=". \n")
print("-3", nombre[-3], end=". \n")
print("-4", nombre[-4], end=". \n")
print("-5", nombre[-5], end=". \n")

# Imprimir un rango
print(nombre[0:2])  # sin incluir el indice 2

# Ir del inicio de la lista al indice (sin incluirlo)
print(nombre[:3])

# Ir desde el indice indicado  hasta el final
print(nombre[2:])

# Cambiar un valor
nombre[3] = "Monet"
print(nombre)

# Iterar una lista
for nombres in nombre:
    print(nombres)
else:
    print("No hay mas nombres en la lista")

# Preguntar la longitud de una lista
print(f" La lista nombre tiene {len(nombre)} elementos")

# Agregar un elemento a la lista
nombre.append("Philip Lenard")
print(nombre)

# Insertar un elemento en un indice proporcionado
nombre.insert(1, "Max Planck")
print(nombre)

# Remover un elemento por valor
nombre.remove("lili")
print(nombre)

# Remover el ultimo valor agregado ala lista
nombre.pop()
print(nombre)

# Eliminar un elemento en un indice indicado
del nombre[0]
print(nombre)

# Limpiar todos los elementos de lista
nombre.clear()
print(nombre)

# Borrar la lista de la memoria ram
del nombre
print(nombre)
