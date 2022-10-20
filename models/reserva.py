from typing import List
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from db import db

class Reserva(db.Model):
    __tablename__ = "reservass"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(100))
    costo = Column(Integer)
    cantidad = Column(Integer)
    empresa = Column(String(100))

    def __init__(self, nombre=None, costo=None, cantidad=None, empresa=None):
        self.nombre = nombre
        self.costo = costo
        self.cantidad = cantidad
        self.empresa = empresa

    def crear(nombre, costo, cantidad, empresa):
        material= Reserva(nombre,costo,cantidad,empresa)
        db.session.add(material)
        db.session.commit()