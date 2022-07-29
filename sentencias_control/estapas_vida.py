#!/usr/bin/python3

edad = int(input("Ingresa tu edad: "))

if 1 <= edad <= 10:
    print("La infancia es increible")
elif 11 <= edad <= 20:
    print("Muchos cambios y mucho estudio")
elif 21 <= edad <= 30:
    print("El 'amor' y comienza el trabajo "[3:-1].upper())
else:
    print("Etapa de", "vida"[::].upper(), "no reconocida")
