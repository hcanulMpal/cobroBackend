from datetime import datetime
import datetime
from ..models import db, Pagos, Personas
from flask import jsonify


base = db.session

class guardarDatos:


    def savePersona(self, data):

        persona = Personas(
            name = data['name'].upper(),
            ap_Pat = data['ap_pat'].upper(),
            ap_mat = data['ap_mat'].upper(),
            tel = data['tel'].upper(),
            RFC = data['RFC'].upper()
        )
        base.add(persona)
        base.commit()
        return Personas.query.filter_by(name =data['nombre']).filter_by(ap_Pat = data['ap_pat'].filter_by(ap_mat = data['ap_mat']).filter_by(tel=data['tel']).filter_by(email =data['email']).filter_by(RFC = data['RFC'].first(id)))


    
  




