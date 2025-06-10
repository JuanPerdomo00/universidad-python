from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = b"tGn'guDXySBdoEn-Z9[:P]PMhD"


@app.route("/")
def inicio():
    if "username" in session:
        return f"El usuario {session['username']} hizo login :D"
    return "NO ha hecho login"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # omitir  validacion de pass y user
        usuario = request.form["username"]
        session["username"] = usuario
        return redirect(url_for("inicio"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("inicio"))
