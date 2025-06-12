from sapflask.app import db


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
