from  dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class servicio_Schema(ma.Schema):
    class Meta: 
        fields = ('id', 'nombre', 'precio')


service = servicio_Schema()
services = servicio_Schema(many=True)