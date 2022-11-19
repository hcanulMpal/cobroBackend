import datetime

class getNum:

    hora = datetime.datetime.now()

    def Gen(self, data):

        folio = str(data)
        newHora = self.hora.strftime('%d%m$y%H%M%S')
        lineadepago = newHora + folio

        return lineadepago
