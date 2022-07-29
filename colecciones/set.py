#!/usr/bin/python3

planetas = {"Venus", "Jupiter", "Saturno", "Neptuno", "Tierra"}
# no tienen orden, ni indices, tampoco acepta item duplucados
print(planetas)

# largo de set
print(len(planetas))

# revisar si un elemento esta presente
print("Venus" in planetas)

# agregar un elemento
planetas.add("Urano")
print(planetas)

# NO se pueden duplicar elementos
planetas.add("Tierra")
print(planetas)

# Eliminar elemento
planetas.remove("Tierras")
planetas.discard("Tierras")
print(planetas)

# eliminar el set
planetas.clear()
print(planetas)

del planetas
print(planetas)