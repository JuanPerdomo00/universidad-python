import requests

# Función que hace una petición HTTP y recibe un callback
def hacer_peticion(url, callback):
    try:
        # Realiza la petición HTTP GET
        respuesta = requests.get(url)
        
        # Verifica si la respuesta fue exitosa
        if respuesta.status_code == 200:
            print("Respuesta recibida con éxito.")
            callback(respuesta.json())  # Llama al callback con los datos recibidos
        else:
            print(f"Error al hacer la petición. Código de estado: {respuesta.status_code}")
            callback(None)  # En caso de error, llamamos al callback con None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        callback(None)

# Callback que maneja los datos recibidos
def manejar_datos(respuesta):
    if respuesta:
        print("Datos recibidos:", respuesta)
    else:
        print("No se pudieron obtener los datos.")

# URL de ejemplo (puedes usar una API real o un endpoint simulado)
url_api = "https://jsonplaceholder.typicode.com/posts/1"

# Llamada a la función hacer_peticion con un callback
hacer_peticion(url_api, manejar_datos)
