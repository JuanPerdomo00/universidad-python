#!/usr/bin/python3

print("Numeros divisibles entre 3")
for i in range(1, 10 + 1):
    if i % 3 == 0:
        print(i)
else:
    print("Numeros de el 2 al 6")
    for i in range(2, 6 + 1):
        print(i)
    else:
        print("rando de 3, 10 pero de 2 en dos")
        for i in range(3, 10 + 1, 2):
            print(i)
