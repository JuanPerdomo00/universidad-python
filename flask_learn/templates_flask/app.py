from flask import Flask, render_template


app = Flask(__name__)


@app.route("/mostrar/<nombre>", methods=["GET", "POST"])
def mostrar_nombre(nombre):
    return render_template("mostrar.html", nombre=nombre)
