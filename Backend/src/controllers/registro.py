from ..functions import fregistro
from ..functions.listaFront import guardarServicios

reg = fregistro()

class registroCtl:

    def getlistPersona(self, data):
        response = reg.guardarDatos(data)
        return response
