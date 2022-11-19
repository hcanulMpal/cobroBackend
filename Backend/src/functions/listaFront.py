from ..models import db, Pagos
from ..functions import getNum
from flask import jsonify


base = db.session

class guardarServicios:

    data = {
        "nombres": "capicp",
        "ap_pat" : "puto",
        "ap_Mat" :"delacalle",
        "telefono": "9838092289",
        "rfc" : "123456",
        "folio" :"123456",
        "servicio_id": "2",

    }

    def saveServicios(self, data, id):

        pago = Pagos(
            folio = data['folio'],
            servicios_id = data['id_servicios'],
            persona_id = id,
            lineaDePago = getNum(self.folio),
              
        )
        base.add(pago)
        base.commit()
        return Pagos.query.filter_by(lineaDePago=getNum(self.folio)).first()






