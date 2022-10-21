from typing import List
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from db import db

class Reserva(db.Model):
    tablename = "reservass"
    id = Column(Integer,primary_key=True)
    costo = Column(Integer)
    cantidad = Column(Integer)
    material = Column(Integer,ForeignKey('materiales.id'))

    def init(self, costo=None, cantidad=None, mID=None):
        self.costo = costo
        self.cantidad = cantidad
        self.material = mID

    def crear(costo, cantidad, mID):
        material= Reserva(costo,cantidad,mID)
        db.session.add(material)
        db.session.commit()