from ..models import db, Pagos
from ..functions import getNum, guardarDatos
from flask import jsonify
from .moneda import money

M = money()
G = guardarDatos()
N = getNum()

base = db.session

class guardarServicios:

    data = {
        "nombres": "capicp",
        "ap_pat" : "maquinadefuego",
        "ap_mat" :"delacalle",
        "telefono": "9838092289",
        "precio": 100.00,
        "rfc" : "123456",
        "folio" : 123456,
        "servicios_id": "2",

    }

    def saveServicios(self, data, id):

        pago = Pagos(
            folio = data['folio'],
            servicios_id = data['servicios_id'],
            precio = M.SetMoneda(data['precio']),
            persona_id = id,
            lineaDePago = N.Gen(data['folio']),
              
        )
        base.add(pago)
        base.commit()
        return Pagos.query.filter_by(lineaDePago= N.Gen(data['folio'])).first()