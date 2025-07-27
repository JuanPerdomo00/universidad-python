def validar_formulario(nombre, edad, callback_success, callback_error):
    if not nombre or edad < 18:
        callback_error("Datos no válidos. Nombre y edad deben ser correctos.")
    else:
        callback_success(f"Formulario enviado correctamente: {nombre}, {edad} años.")

def mostrar_mensaje_exito(mensaje):
    print(mensaje)

def mostrar_mensaje_error(mensaje):
    print(f"Error: {mensaje}")

# Aplicación real: Validar los datos del formulario y realizar una acción en función del resultado
validar_formulario("Juan", 20, mostrar_mensaje_exito, mostrar_mensaje_error)
validar_formulario("", 15, mostrar_mensaje_exito, mostrar_mensaje_error)
