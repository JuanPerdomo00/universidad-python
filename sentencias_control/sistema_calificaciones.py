#!/usr/bin/python3

estudiante = input("Ingrese su nombre: ")
nota = int(input("Ingresa tu nota de examen de fisica: "))

if 9 <= nota <= 10:
    print(f"Bienvenido a la academia prusiana Sr {estudiante.capitalize()} su nota fue de {nota} A+")
else:
    if 8 <= nota < 9:
        print(f"Bienvenido a la academia prusiana Sr {estudiante.capitalize()} su nota fue de {nota} B")
    else:
        if 7 <= nota < 8:
            print(f"Su nota fue de {nota} C por favor repita el examen Sr {estudiante.capitalize()}")
        else:
            if 6 <= nota < 7:
                print(f"Su nota fue de {nota} D por favor repita el examen Sr {estudiante.capitalize()}")
            else:
                if 5 <= nota < 6:
                    print(f"Su calificacion fue de {nota} F muy baja Sr {estudiante.capitalize()}")
                else:
                    if 4 <= nota < 5:
                        print(f"Su calificacion fue de {nota} F muy baja Sr {estudiante.capitalize()}")
                    else:
                        if 3 <= nota < 4:
                            print(f"Su calificacion fue de {nota} F muy baja Sr {estudiante.capitalize()}")
                        else:
                            if 2 <= nota < 3:
                                print(f"Su calificacion fue de {nota} F muy baja Sr {estudiante.capitalize()}")
                            else:
                                if 0 <= nota < 2:
                                    print(f"Su calificacion fue de {nota} F muy baja Sr {estudiante.capitalize()}")
                                else:
                                    print(f"Proporsiona un valor de 0-10 Sr {estudiante.capitalize()}")

