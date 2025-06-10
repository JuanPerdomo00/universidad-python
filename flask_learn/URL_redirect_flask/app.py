from flask import Flask, url_for, redirect, render_template
import platform

app = Flask(__name__)


@app.route("/")
def home():
    return f"Home :D {platform.system()} --> Your os"


@app.route("/saludar/<name>")
def saludar(name: str):
    return render_template("mostrar.html", name=name)


@app.route("/redirection")
def redirection():
    return redirect(url_for("home"))
