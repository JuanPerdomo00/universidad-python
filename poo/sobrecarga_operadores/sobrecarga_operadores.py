#!/usr/bin/python3

# Sobregarga de operadores significa que un operador se puede comportar de dieferentes formas

# Operador de suma + se comporta diferente tanto con tipos int, string y lista
# Dependiendo de el tipo de operador con el que este trabajando, asi sera el comportamiento
# que este tomara

# Un mismo operador puede trabajar de distintas formas
a = 2
b = 3
print(a + b)  # operador de suma

a = "Hola"
b = " Mundo"
print(a + b)  # concatenacion

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # Se genera una sola lista con la union de a y b


mi_objeto1 + mi_objeto2
