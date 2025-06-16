import sys 

DIGITS = 100**3

sys.set_int_max_str_digits(DIGITS)
def fibonacci():
    a, b = 0, 1
    while True:  # Genera los números infinitamente
        yield a
        a, b = b, a + b

# Aplicación práctica: Obtener los primeros 10 números de la secuencia de Fibonacci
fib_gen = fibonacci()

for i in range(1, DIGITS):
    print(next(fib_gen))