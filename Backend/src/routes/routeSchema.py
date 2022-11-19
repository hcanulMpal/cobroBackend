from flask import Blueprint
from flask_cors import CORS
from ..controllers import ServiciosCtl
from ..controllers import registroCtl
from ..functions import guardarServicios
import requests

guard = guardarServicios().data

landing = Blueprint('admini', __name__)
cors = CORS(landing, resources={ r"/api/*":{"origins":"*"}})

servi = ServiciosCtl()
re = registroCtl()

@landing.route("/api/landing/servicios", methods=['GET'])
def setservicios():
    return servi.setserviciosomg()


@landing.route("/api/landing/serviciospost", methods=['POST'])
def getlistPersona():
    return print ("Llego aqui")
    #return re.getlistPersona(guard)



    



