"""
from ..models import db, Pagos
from .fServ import funcServ

base = db.session

class funcPago():

    p1 = {
        "folio": '',
        "servicios_id": '',
        "persona_id": '',
        "lineaDePago": '',
        "servicios_id": 'Luz',
    }
    p2 = {
        "nombre": 'Alma Sarai Canche Chan',
        "direccion": 'Calle su casa x su colonia',
        "telefono": '9832021647',
        "servicios_id": 'Agua',
        "lineaDePago": '8367456789',
    }
    p3 = {
        "nombre": 'Jose Alejandro Tun Xool',
        "direccion": 'Calle su casa x su colonia',
        "telefono": '9838092289',
        "servicios_id": 'Terreno',
        "lineaDePago": '7638254678',
    }
    p4 = {
        "nombre": 'Eliud Carmona',
        "direccion": 'Calle su casa x su colonia',
        "telefono": '9831764171',
        "servicios_id": 'Luz',
        "lineaDePago": '9865745623',
    }
    p5 = {
        "nombre": 'Alex Jhovani Velazques Chi',
        "direccion": 'Calle su casa x su colonia',
        "telefono": '9831162738',
        "servicios_id": 'Terreno',
        "lineaDePago": '6754578654',
    }


    def is_Data(self):
        if not Pagos.query.all():
            self.savePagos(self.p1)
            self.savePagos(self.p2)
            self.savePagos(self.p3)
            self.savePagos(self.p4)
            self.savePagos(self.p5)

    def savePagos(self, data):
        pag = Pagos(
            nombre = data['nombre'],
            direccion = data['direccion'],
            telefono = data['telefono'],
            servicios_id = funcServ().findServicioPago(data['servicios_id']),
            lineaDePago = data['lineaDePago'],
        )
        base.add(pag)
        base.commit()
"""