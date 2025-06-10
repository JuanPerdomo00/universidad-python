from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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