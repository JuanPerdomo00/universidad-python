#!/usr/bin/python3

# Dada la siguiente tupla,
# crear una lista que solo incluya los numeros menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = [i for i in tupla if i < 5]
print(lista)
