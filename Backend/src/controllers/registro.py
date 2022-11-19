from ..functions import fregistro

reg = fregistro()

class fregistro:

    def getlistPersona(self, data):
        response = reg.guardarDatos(data)
