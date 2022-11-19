from ..models import db, Pagos
from functions import getNum
from flask import jsonify


base = db.session

class guardarServicios:

    def saveServicios(self, data, id):

        pago = Pagos(
            folio = data['folio'],
            servicios_id = data['id_servicios'],
            persona_id = data['id_persona'],
            lineaDePago = getNum(self.folio),
              
        )
        base.add(pago)
        base.commit()
        return Pagos.query.filter_by(lineaDePago=getNum(self.folio)).first()






