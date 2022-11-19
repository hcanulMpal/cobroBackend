from ..models import Persona, db

base = db.session

class dbPersona:

    def findPersonaNombre(self, name):
        return Persona.query.filter_by(nombre=name).first().id
