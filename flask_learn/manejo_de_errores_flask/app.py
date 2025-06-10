from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Inicio"


@app.route('/exit')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    print(error)
    return render_template("error404.html", error=error), 404