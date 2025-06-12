from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from sapflask.database import db
from sapflask.models import Persona
from sapflask.forms import PersonaForm

app = Flask(__name__)

# COnfiguracion de la db
USER_DB = "jakepys"
PASS_DB = "123chopin"
URL_DB = "localhost"
NAME_DB = "sap_flask_db"
FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}"

app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializacion del objeto SQLALCHEMY
db.init_app(app)

# Configurar flask_migrate
migrate = Migrate()
migrate.init_app(app, db)


# Configurar flask-wtf
app.config["SECRET_KEY"] = "=g%7}gBQpK;Oc;3Qx~#=;yLe[L"


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def inicio():
    # Listado de personas
    #personas = Persona.query.all()
    personas = Persona.query.order_by("id")
    total_personas = Persona.query.count()
    app.logger.debug(f"Listado de personas: {personas}")
    app.logger.debug(f"Total personas: {total_personas}")
    return render_template(
        "index.html", personas=personas, total_personas=total_personas
    )


@app.route("/verp/<int:id>")
def ver_persona(id: int):
    # recuperamos la persona segun el ID
    persona = Persona.query.get_or_404(id, "No se encontro la persona")
    app.logger.debug(f"Persona recuperada: {persona}")
    app.logger.debug(f"Type: {type(persona)}")
    return render_template("detalle.html", persona=persona)


@app.route("/agregar", methods=["GET", "POST"])
def agregar_persona():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)

    if request.method == "POST":
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(f"Persona a insertar: {persona}")
            # insertamos nuevo registro
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for("inicio"))

    return render_template("agregar.html", forma=personaForm)


@app.route("/editarp/<int:id>", methods=["GET", "POST"])
def editar_persona(id):
    persona = Persona().query.get_or_404(id, "No se encontro la persona")
    personaForm = PersonaForm(obj=persona)
    if request.method == "POST":
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(persona)
            db.session.commit()
            return redirect(url_for("inicio"))
    return render_template("editar.html", forma=personaForm)


@app.route("/eliminarp/<int:id>")
def eliminar_persona(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f"Persona a eliminar: {persona}")
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for("inicio"))
