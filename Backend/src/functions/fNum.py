import datetime

hora = datetime.datetime.now()

class getNum:

    def Gen(self, data):

        folio = str(data)
<<<<<<< Updated upstream
        newHora = hora.strftime('%d%m$y%H%M%S')
        lineadepago = newHora + folio
=======
        newHora = self.hora.strftime('%d%m%y%H%M%S')
        lineaDePago = newHora + folio
>>>>>>> Stashed changes

        return lineaDePago
