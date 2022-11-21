from ..models import db, Servicios
from ..schemas import services, service

base = db.session

class funcServ():
    luz = [
        {
            "nombre": 'TRAMITE DE RENOVACION DE LICENCIAS DE CONDUCIR',
            "precio": 1.00,
        },
        {
            "nombre": 'LICENCIA DE CONDUCIR CHOFER',
            "precio": 262.00,
        },
        {
            "nombre": 'LICENCIA DE CONDUCIR MOTOCICLISTA',
            "precio": 394.00,
        },
        {
            "nombre": 'LICENCIA DE CONDUCIR AUTOMOVILISTA',
            "precio": 351.00,
        },
        {
            "nombre": 'LICENCIA DE CONDUCIR SERVICIO PÚBLICO',
            "precio": 590.00,
        },
        {
            "nombre": 'LICENCIA DE CONDUCIR EXTRANJEROS',
            "precio": 885.00,
        },
        {
            "nombre": 'TRÁMITE DE PERMISO PROVISIONAL PARA MENOR DE EDAD 30 DIAS',
            "precio": 1.00,
        },
        {
            "nombre": 'TRÁMITE DE PERMISO PROVISIONAL PARA MENOR DE EDAD 60 DIAS',
            "precio": 1.00,
        },
        {
            "nombre": 'TRÁMITE DE PERMISO PROVISIONAL PARA MENOR DE EDAD 90 DÍAS',
            "precio": 437.00,
        },
        {
            "nombre": 'TRAMITE DE RENOVACION DE LICENCIA DE CONDUCIR CHOFER',
            "precio": 262.00,
        },
        {
            "nombre": 'TRAMITE DE RENOVACION DE LICENCIA DE CONDUCIR MOTOCICLISTA',
            "precio": 394.00,
        },
        {
            "nombre": 'TRAMITE DE RENOVACION DE LICENCIA DE CONDUCIR AUTOMOVILISTA',
            "precio": 351.00,
        },
        {
            "nombre": 'TRAMITE DE RENOVACION DE LICENCIA DE CONDUCIR SERVICIO PUBLICO',
            "precio": 1.00,
        },
        {
            "nombre": 'DIVORCIO ADMINISTRATIVO',
            "precio": 3674.80,
        },
        {
            "nombre": 'REGISTRO DE RECONOCIMIENTO CON LA CERTIFICADA',
            "precio": 627.72,
        },
        {
            "nombre": 'REGISTRO DE RECONOCIMIENTO SIN LA CERTIFICADA',
            "precio": 448.48,
        },
        {
            "nombre": 'DIVORCIO JURIDICO',
            "precio": 1.00,
        },
        {
            "nombre": 'REGISTRO DE DEFUNCIONES',
            "precio": 1255.06,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO ENTRE MEXICANOS (EN LAS OFICINAS EN HORAS HABILES)',
            "precio": 403.29,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO ENTRE MEXICANOS (EN LAS OFICINAS EN HORAS INHABILES)',
            "precio": 627.34,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO ENTRE MEXICANOS (FUERA DE LAS OFICINAS EN HORAS HABILES)',
            "precio": 806.58,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO ENTRE MEXICANOS (FUERA DE LAS OFICINAS EN HORAS INHABILES)',
            "precio": 985.82,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO ENTRE MEXICANOS EN SAB. DOM. Y DIAS FESTIVOS',
            "precio": 1971.64,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO',
            "precio": 3898.47,
        },
        {
            "nombre": 'SERVICIO NUEVO',
            "precio": 4794.67,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO ENTRE MEXICANOS Y EXTRANJEROS EN LAS OFICINAS',
            "precio": 7035.17,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO ENTRE MEXICANOS Y EXTRANJEROS FUERA DE LAS OFICINAS',
            "precio": 11516.20,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO ENTRE EXTRANJEROS EN LAS OFICINAS',
            "precio": 268.86,
        },
        {
            "nombre": 'REGISTRO DE MATRIMONIO ENTRE EXTRANJEROS FUERA DE LAS OFICINAS',
            "precio": 1165.06,
        },
        {
            "nombre": 'TERRENO  EN EL PANTEON COSTO  POR  METRO CUADRADO',
            "precio": 388.35,
        },
        {
            "nombre": 'TERRENO EN EL PANTEÓN PERSONA ADULTA',
            "precio": 376.48,
        },
        {
            "nombre": 'TERRENO EN EL PANTEÓN NIÑOS',
            "precio": 179.24,
        },
        {
            "nombre": 'TERRENO EN EL PANTEÓN  R.N.',
            "precio": 268.86,
        },
        {
            "nombre": 'TRASLADO DE CADAVER DE UN MUNICIPIO A OTRO',
            "precio": 716.96,
        },
        {
            "nombre": 'TRASLADO DE CADAVER DE UN MUNICIPIO A OTRO ESTADO',
            "precio": 89.62,
        },
        {
            "nombre": 'TRASLADO DE CADAVER DE UN MUNICIPIO AL EXTRANJERO',
            "precio":  134.43,
        },
        {
            "nombre": 'TRASLADO DE RESTOS ÁRIDOS DE UN MUNICIPIO A OTRO',
            "precio": 627.34,
        },
        {
            "nombre": 'TRASLADO DE RESTOS ÁRIDOS DE UN MUNICIPIO A OTRO ESTADO',
            "precio": 425.24,
        },
        {
            "nombre": 'TRASLADO DE RESTOS ÁRIDOS DE UN MUNICIPIO AL EXTRANJERO',
            "precio":  762.24,
        },
        {
            "nombre": 'ACTAS FORANEAS DE  NACIMIENTOS',
            "precio":  762.24,
        },
        {
            "nombre": 'ACTAS FORANEAS DE  MATRIMONIOS',
            "precio": 179.24,
        },
        {
            "nombre": 'ACTAS FORANEAS DE DEFUNCIONES',
            "precio": 313.67,
        },
        {
            "nombre": 'ACTAS CERTIFICADAS DE NACIMIENTO',
            "precio": 179.24,
        },
        {
            "nombre": 'ACTAS CERTIFICADAS DE MATRIMONIO',
            "precio": 358.48,
        },
        {
            "nombre": 'ACTAS CERTIFICADAS DE DEFUNCIÓN',
            "precio": 179.24,
        },
        {
            "nombre": 'ACTAS CERTIFICADAS DE DIVORCIO',
            "precio": 358.48,
        },
        {
            "nombre": 'ACTAS CERTIFICADAS DE RECONOCIMIENTO',
            "precio": 985.82,
        },
        {
            "nombre": 'ACTAS CERTIFICADAS DE ADOPCIÓN',
            "precio": 179.24,
        },
        {
            "nombre": 'REGISTRO DE ADOPCIÓN',
            "precio": 89.62,
        },
        {
            "nombre": 'CONSTANCIA DE  INEXISTENCIA',
            "precio": 89.62,
        },
        {
            "nombre": 'CERTIFICACIÓN DE DOCUMENTOS',
            "precio": 44.81,
        },
        {
            "nombre": 'ANOTACIÓN MARGINAL',
            "precio": 179.24,
        },
        {
            "nombre": 'COPIA LIBRO',
            "precio": 1.00,
        },
        {
            "nombre": 'BUSQUEDAS',
            "precio": 1.00,
        },
    ]

    def is_Data(self):
        if not Servicios.query.all():
            for item in self.luz:
                self.saveServ(item)
        return True, 200
    

    def saveServ(self, data):
        serv = Servicios(
            nombre = data['nombre'],
            precio = data['precio'],
        )
        base.add(serv)
        base.commit()

    def setservice(self):
        return services.jsonify(Servicios.query.all())


