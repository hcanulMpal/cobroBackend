from ..models import db, Servicios

base = db.session

class funcServ():
    luz = {
        "name": 'Luz',
        "precio": 200,
    }

    def is_Data(self):
        if not Servicios.query.all():
            pass
    

    def saveServ(self, data):
        serv = Servicios(
            name = data['name'],
            precio = data['precio'],
        )
        base.add(serv)
        base.commit()