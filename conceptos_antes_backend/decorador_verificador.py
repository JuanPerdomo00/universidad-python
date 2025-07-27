# Decorador para verificar que los parámetros sean positivos
def verificar_positivo(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                print(f"Error: {arg} no es un número positivo.")
                return
        return func(*args, **kwargs)
    return wrapper

# Función que realiza una operación (por ejemplo, multiplicar dos números)
@verificar_positivo()
def multiplicar(a, b):
    return a * b

# Intentar con números negativos
print(multiplicar(5, -3))  # Debería mostrar un error por el número negativo

# Intentar con números positivos
print(multiplicar(5, 3))  # Debería ejecutar la multiplicación correctamente