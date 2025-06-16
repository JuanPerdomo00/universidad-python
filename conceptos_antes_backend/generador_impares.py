def generador_impares(limite):
    num = 1
    while num <= limite:
        yield num
        num += 2

# Aplicación práctica: Obtener los primeros 10 números impares
for numero in generador_impares(20):
    print(numero)