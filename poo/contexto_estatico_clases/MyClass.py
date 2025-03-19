#!/usr/bin/python3


class Mi_Calse:
    var_clase = "Valor de variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


if __name__ == "__main__":
    # variable de objeto
    print(Mi_Calse.var_clase)

    # crear objeto para acceder a self
    var1 = Mi_Calse("Variable de instancia self")
    print(var1.variable_instancia)

    # despues de haber creado nuestro objeto, podemos asociar una nueva variable
    Mi_Calse.var_clase_2 = "Nueva variable clase 2"

    var2 = Mi_Calse("Variable de self diferente")
    print(var2.var_clase)
    print(var2.variable_instancia)

    print(Mi_Calse.var_clase_2)
    print(var2.var_clase_2)  # <- el ide no la reconoce divido a que se creo en vuelo
