from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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
db = SQLAlchemy(app)

# Configurar flask_migrate
migrate = Migrate()
migrate.init_app(app, db)


class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(250))
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __str__(self):
        return (
            f"Id: {self.id}, "
            f"Nick Name: {self.nick_name}, "
            f"Nombre: {self.nombre}, "
            f"Apellido: {self.apellido}, "
            f"Email: {self.email}, "
        )


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def inicio():
    # Listado de personas
    personas = Persona.query.all()
    total_personas = Persona.query.count()
    app.logger.debug(f"Listado de personas: {personas}")
    app.logger.debug(f"Total personas: {total_personas}")
    return render_template(
        "index.html", personas=personas, total_personas=total_personas
    )


@app.route('/verp/<int:id>')
def ver_persona(id: int):
    # recuperamos la persona segun el ID
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f"Persona recuperada: {persona}")
    app.logger.debug(f"Type: {type(persona)}")
    return render_template("detalle.html", persona=persona)
