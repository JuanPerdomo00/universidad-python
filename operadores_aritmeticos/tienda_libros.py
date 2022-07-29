#!/usr/bin/python3

print("Tienda de libros \n")
nombre_libro, Id = input("Ingrese nombre de el libro: "), int(input("Ingrese ID de el libro: "))

precio, envio = float(input("Ingresa el precio de el libro: ")), bool(input("Envio gratuito (True o False): "))

if envio:
    pass

else:
    pass

print("-"*40)
print(f"""
Nombre libro: {nombre_libro}
ID: {Id}
Precio Libro: {precio}
Envio Gratis? {envio}
""")
print("-"*40)
