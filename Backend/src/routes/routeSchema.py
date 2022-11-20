from flask import Blueprint, request
from flask_cors import CORS
from ..controllers import ServiciosCtl
from ..controllers.registro import registroCtl
from ..controllers import guardarServicios

guard = guardarServicios().data
guarda = guardarServicios()

landing = Blueprint('admini', __name__)
cors = CORS(landing, resources={ r"/api/*":{"origins":"*"}})

servi = ServiciosCtl()
re = registroCtl()

@landing.route("/api/landing/servicios", methods=['GET'])
def setservicios():
    return servi.setserviciosomg()


@landing.route("/api/landing/serviciospost", methods=['POST'])
def getlistPersona():
    #re.getlistPersona(guard)
    guarda.saveServicios(guard, re.getlistPersona(guard))
    print ("Llego aqui verdad")


    



