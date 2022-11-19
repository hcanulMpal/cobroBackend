from datetime import datetime
import datetime
from ..models import db, Persona
from flask import jsonify


base = db.session

class guardarDatos:


    def savePersona(self, data):

        persona = Persona(
            nombres = data['nombres'].upper(),
            ap_Pat = data['ap_pat'].upper(),
            ap_Mat = data['ap_Mat'].upper(),
            telefono = data['telefono'].upper(),
            rfc = data['rfc'].upper()
        )
        base.add(persona)
        base.commit()
        return Persona.query.filter_by(nombres =data['nombres']).filter_by(ap_Pat = data['ap_pat'].filter_by(ap_Mat = data['ap_mat']).filter_by(telefono=data['telefono']).filter_by(rfc = data['rfc'].first(id)))


    
  




