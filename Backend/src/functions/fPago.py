from ..models import db, Pagos

base = db.session

class dbPagos:

    def savePagos(self, data, id):
        pago = Pagos (
            
        )