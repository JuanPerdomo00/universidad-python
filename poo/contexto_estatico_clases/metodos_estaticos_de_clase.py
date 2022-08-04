#!/usr/bin/python3

class Mi_Calse:
    var_clase = "Valor de variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(Mi_Calse.var_clase)

    # metodo de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.var_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()


Mi_Calse.metodo_clase()

objeto1 = Mi_Calse("Variable de instancia")
objeto1.metodo_clase()

objeto1.metodo_instancia()
