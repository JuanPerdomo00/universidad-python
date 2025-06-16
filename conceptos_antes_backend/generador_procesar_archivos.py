def leer_lineas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            yield linea.strip()  # Elimina el salto de línea al final de cada línea

# Aplicación práctica: Leer líneas de un archivo grande
for linea in leer_lineas('archivo_grande.txt'):
    print(linea)
