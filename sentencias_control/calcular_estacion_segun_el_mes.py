#!/usr/bin/python3

mes = int(input("Ingresa el mes de el año: "))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else:
    estacion = "Mes incorrecto, descubriste un mes xd"
    print(f"Mes no existe, {estacion}")
    exit()

print(f"Para el mes {mes} la estacion es {estacion}")
