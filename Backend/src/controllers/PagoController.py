from ..functions.fServ import funcServ
import requests

pag = funcServ()

class ServiciosCtl:

    def setserviciosomg(self):
        return pag.setservicio()
