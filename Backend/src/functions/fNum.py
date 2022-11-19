import datetime

hora = datetime.datetime.now()

class getNum:

    def Gen(self, data):

        folio = str(data)
        newHora = hora.strftime('%d%m$y%H%M%S')
        lineadepago = newHora + folio

        return lineadepago
