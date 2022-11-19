from ..functions.fServ import funcServ
from ..functions.fPago import funcPago

def verifyAndCreateData():

    services = funcServ().is_Data()
    pagos = funcPago().is_Data()