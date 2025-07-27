import time

# Decorador para medir el tiempo de ejecución de una función
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Tiempo antes de la ejecución
        resultado = func(*args, **kwargs)  # Ejecuta la función original
        fin = time.time()  # Tiempo después de la ejecución
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio:.4f} segundos.")
        return resultado
    return wrapper

# Aplicamos el decorador a una función
@medir_tiempo
def hacer_calculos():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

# Llamamos a la función
hacer_calculos()
