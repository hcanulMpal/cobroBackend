from ..models import db, dbServicios

base = db.session

class funcServ():
    luz = {
        "name": 'Luz',
        "precio": 200,
    }

    def is_Data(self):
        if not dbServicios.query.all():
            pass
    

    def saveServ(self, data):
        serv = dbServicios(
            name = data['name'],
            precio = data['precio'],
        )
        base.add(serv)
        base.commit()