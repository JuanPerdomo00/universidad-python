import time

def descargar_archivo(url, callback):
    print(f"Descargando archivo desde {url}...")
    time.sleep(3)  # Simulamos que la descarga tarda 3 segundos
    print("Archivo descargado.")
    callback()  # Llamamos al callback después de la descarga

def notificar_descarga_completa():
    print("¡Descarga completa! Puedes abrir el archivo ahora.")

# Aplicación real: descargar un archivo y realizar una acción cuando termine
descargar_archivo("https://ejemplo.com/archivo.zip", notificar_descarga_completa)
