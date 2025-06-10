from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    app.logger.info(f"Entrando desde el path {request.path}")
    return "Hello World"


@app.route("/saludar/<name>")
def saludar_user(name: str):
    return f"Hola, {name} all good?"


@app.route("/edad/<int:edad>")
def mostrar_edad(edad: int):
    return (
        "Estas muerto"
        if edad >= 120
        else "Eres anciano"
        if edad >= 70 < 120
        else "Eres un jovencito"
        if edad >= 7 <= 18
        else "Eres un bebe que haces aqui"
        if edad > 0 <= 6
        else "What?"
    )
