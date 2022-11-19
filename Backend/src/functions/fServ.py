from ..schemas.schema_Pago import pago, pagos

from ..models import db, Servicios

base = db.session

class funcServ():
    luz = {
        "nombre": 'Luz',
        "precio": 200,
    }
    agua = {
        "nombre": 'Agua',
        "precio": 500,
    }
    tierra = {
        "nombre": 'Terreno',
        "precio": 100,
    }

    def is_Data(self):
        if not Servicios.query.all():
            self.saveServ(self.luz)
            self.saveServ(self.agua)
            self.saveServ(self.tierra)
    

    def saveServ(self, data):
        serv = Servicios(
            nombre = data['nombre'],
            precio = data['precio'],
        )
        base.add(serv)
        base.commit()


    def findServicesNombre(self, name):
        return Servicios.query.filter_by(nombre=name).first().id

    def setservicio(self):
        return pagos.jsonify(Servicios.query.all())

