from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Servicios(db.Model):
    __tablename__ = 'servicios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) 
    pagos = db.relationship(
        'Pagos',
        uselist=False,
        backref='Servicios',
        lazy=True,
    )

class Pagos(db.Model):
    __tablename__ = 'pagos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    folio = db.Column(db.String(20), nullable=False)
    servicios_id = db.Column(db.Integer, db.ForeignKey('servicios.id', ondelete='SET NULL'), nullable = True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id', ondelete='SET NULL'), nullable = True)
    precio = db.Column(db.Float, nullable=False)
    lineaDePago = db.Column(db.String(20), nullable= False, unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) 


class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombres = db.Column(db.String(50), nullable =False)
    ap_Pat = db.Column(db.String(20), nullable=False)
    ap_Mat = db.Column(db.String(20), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    rfc = db.Column(db.String(16), unique=True, nullable=False)
    pagos = db.relationship(
        'Pagos',
        uselist=False,
        backref='Personas',
        lazy=True
    )