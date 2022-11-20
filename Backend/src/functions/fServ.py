from ..models import db, Servicios

base = db.session

class funcServ():
    luz = [
        {
            "nombre": 'Luz',
            "precio": 200,
        },
        {
            "nombre": 'Agua',
            "precio": 500,
        },
        {
            "nombre": 'Terreno',
            "precio": 100,
        }
    ]

    def is_Data(self):
        if not Servicios.query.all():
            for item in self.luz:
                self.saveServ(item)
        return True, 200
    

    def saveServ(self, data):
        serv = Servicios(
            name = data['name'],
            precio = data['precio'],
        )
        base.add(serv)
        base.commit()