#!/usr/bin/python3

# extend list
a = [1, 2, 3, 4, 5]
print(a)

a.extend([6, 7, 8, 9])
print(a)

# index
index = a.index(8)
print(index)

# reverse
a.reverse()
print(a)

# menor a mayor
a.sort()  # ascendente
print(a)
# ordenar de mandera desendente
a.sort(reverse=True)  # desendente
print(a)

# valor minimo y maxiomo de una lista
print(max(a))
print(min(a))

# copiar los elementos de una lista
b = a.copy()
print(id(a))
print(id(b))

# misma referencia?
print(id(a) is id(b))
print(a == b)

# slicing
b = a[:]
print(a)

# Mult list

c = 5 * [[3.14]]
print(c)
print(c[0] is c[-1])
print("Misma referencia")
for i, j in enumerate(c):
    try:
        print(f"{i} {j} == {i+1} {c[i+1]} {c[i] is c[i+1]}")
    except IndexError:
        pass

c[1].append("Jakepys")
print(c)

# matreces
m = [
    ["Jakepys", "Aron"],
    ["Richad Stallman", "Linus", "marak"],
    ["abc", "dfg", "hij", "klm"],
]

# obtener a jakepys
print(m[0][0])
# Obtener a linus
print(m[1][1])
# obtener klm
print(m[-1][-1])

n = [
    [103, 107, 109, 113, 127, 131, 137, 139, 149],
    [163, 167, 173, 179, 181, 191, 193, 197],
    [227, 229, 233, 239, 241, 251, 257],
    [281, 283, 293, 307, 311, 313],
    [353, 359, 367, 373, 379],
    [421, 431, 433, 439],
    [487, 491, 499],
    [569, 571],
    [631],
    [],
]

# ordenar por el largo de listas
n.sort(key=len)
print(n)

# sorted built-in
names = ["natalia michael", "valeria tovar", "natalia martines", "Flor valeriano", "ximena sanchez"]
names = sorted(names)
print(names)

# desendente
names = sorted(names, reverse=True)
print(names)


