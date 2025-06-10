from flask import Flask

app = Flask(__name__)


@app.route("/mostrar/<nombre>", methods=["GET", "POST"])
def mostrar_nombre(nombre):
    return f"{nombre}"
