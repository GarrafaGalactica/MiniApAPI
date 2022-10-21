from typing import List
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from db import db
from models.material import Material

class Reserva(db.Model):
    tablename = "reservass"
    id = Column(Integer,primary_key=True)
    costo = Column(Integer)
    cantidad = Column(Integer)
    material = Column(Integer,ForeignKey('materiales.id'))
    estado = Column(String(100))

    def __init__(self, costo=None, cantidad=None, mID=None):
        self.costo = costo
        self.cantidad = cantidad
        self.material = mID
        self.estado = "iniciado"

    def crear(cantidad, mID):
        costoT = Material.buscarCosto(mID)
        intCan = int(cantidad)
        costoTe = costoT * intCan
        reserva = Reserva(costoTe,cantidad,mID)
        db.session.add(reserva)
        db.session.commit()
        return reserva.id