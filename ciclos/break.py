#!/usr/bin/python

letra = "Dinamarca"

print(letra[5:6])

for letras in letra:
    if letras == "a":
        print(f"Letra encontrada {letras} en el indice {len(letras)}")
        break
else:
    print("Fin de el ciclo")

