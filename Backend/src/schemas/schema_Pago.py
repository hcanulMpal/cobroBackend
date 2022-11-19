from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class Pago_Schema(ma.Schema):
    class Meta:
        fields = ('id','nombre')

pago = Pago_Schema()
pagos = Pago_Schema(many=True)


