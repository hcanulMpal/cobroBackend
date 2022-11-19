from flask import Blueprint
from flask_cors import CORS
from ..controllers import ServiciosCtl
from ..controllers.registro import fregistro


landing = Blueprint('admini', __name__)
cors = CORS(landing, resources={ r"/api/*":{"origins":"*"}})

servi = ServiciosCtl()
re = fregistro()

@landing.route("/api/landing/servicios", methods=['GET'])
def setservicios():
    return servi.setserviciosomg()


@landing.route("/api/landing/serviciospost", methods=['POST'])
def getservicios():
    return re.getdata(request.json)


    



