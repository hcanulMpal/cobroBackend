import datetime

hora = datetime.datetime.now()

class getNum:

    def Gen(self, data):

        folio = str(data)
        newHora = self.hora.strftime('%d%m%y%H%M%S')
        lineaDePago = newHora + folio

        return lineaDePago
