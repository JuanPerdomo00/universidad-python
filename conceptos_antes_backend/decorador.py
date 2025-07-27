# Este es un decorador que añade un comportamiento antes y después de la ejecución de una función
def mi_decorador(func):
    def envoltorio():
        print("Antes de ejecutar la función")
        func()  # Llamamos a la función original
        print("Después de ejecutar la función")
    return envoltorio  # Devolvemos la nueva función envoltorio

# Usamos el decorador en una función con @
@mi_decorador
def saludar():
    print("Hola, ¿cómo estás?")

# Llamamos a la función saludar
saludar()
print(globals())
