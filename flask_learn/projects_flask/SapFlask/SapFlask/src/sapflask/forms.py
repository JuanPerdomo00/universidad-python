from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PersonaForm(FlaskForm):
    nick_name = StringField("nick_name", validators=[DataRequired()])
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])

    # Botones
    enviar = SubmitField("Enviar")
