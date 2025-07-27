# Simulación de un sistema de autenticación
usuario_autenticado = False  # Supongamos que el usuario no está autenticado

# Decorador para verificar si el usuario está autenticado
def verificar_autenticacion(func):
    def wrapper(*args, **kwargs):
        print(args)
        if not usuario_autenticado:
            print("Acceso denegado: el usuario no está autenticado.")
            return
        return func(*args, **kwargs)
    return wrapper

# Aplicamos el decorador a una función
@verificar_autenticacion
def realizar_accion_secreta(password):
    print("Acción secreta realizada con éxito.")

# Intentamos realizar la acción
realizar_accion_secreta("123asd456")

"""
Actividad:

Actualiza el decorador para que verifique una contraseña que reciba la funcion realizar accion secreta

"""
