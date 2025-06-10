from flask import Flask, request

app = Flask("__flask__")


@app.route("/api/mostrar/<nombre>", methods=["GET", "POST"])
def mostrar_json(nombre: str):
    valores = {
        "nombre": nombre,
        "method_http": request.method,
        "content_type": request.content_type,
    }
    return valores
