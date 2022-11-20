from ..functions.fregistro import guardarDatos


ga = guardarDatos()

class registroCtl:

    def getlistPersona(self, data):
        response = ga.savePersona(data)
        return response
