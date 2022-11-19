from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class dbServicios(db.Model):
    __tablename__ = 'servicios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) 
