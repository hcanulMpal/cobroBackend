from ..models import db, dbServicios
from ..schemas.schema_Pago import pago, pagos


base = db.session

class funcServ():
    luz = {
        "nombre": 'Luz',
        "precio": 200,
    }
    agua = {
        "nombre": 'Agua',
        "precio": 5000,
    }
    tierra = {
        "nombre": 'Terreno',
        "precio": 10000000,
    }

    def is_Data(self):
        if not dbServicios.query.all():
            self.saveServ(self.luz)
            self.saveServ(self.agua)
            self.saveServ(self.tierra)
    

    def saveServ(self, data):
        serv = dbServicios(
            nombre = data['nombre'],
            precio = data['precio'],
        )
        base.add(serv)
        base.commit()


    def setservicio(self):
        return pagos.jsonify(dbServicios.query.all())

