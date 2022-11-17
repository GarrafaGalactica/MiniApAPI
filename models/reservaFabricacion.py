from typing import List
from unittest import result
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update, and_
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from db import db
from datetime import date

class ReservaFabricacion(db.Model):
    __tablename__ = "reservasFabricacion"
    id = Column(Integer,primary_key=True)
    fabricante = Column(Integer,ForeignKey('fabricantes.id'))
    fecha_inicio = Column(DateTime)
    fecha_final = Column(DateTime)
    fecha_entrega = Column(DateTime)
    estado = Column(String(100))

    def __init__(self, fabricante=None, fecha_estimada=None):
        self.fabricante = fabricante
        self.fecha_estimada = fecha_estimada
        self.estado = "fabricando"

    def crear(fabricante, fecha):
        reserva= ReservaFabricacion(fabricante,fecha)
        db.session.add(reserva)
        db.session.commit()
        return reserva.id
    
    def retrasar(id):
        reserva = ReservaFabricacion.query.filter_by(id=id).first()
        reserva.estado = "retrasado"
        db.session.commit()
    
    def finalizar(id):
        reserva = ReservaFabricacion.query.filter_by(id=id).first()
        reserva.estado = "finalizado"
        reserva.fecha_entrega = date.today()
        db.session.commit()
    
    def listar():
        return ReservaFabricacion.query.all()

    def buscarReserva(id):
        return ReservaFabricacion.query.filter_by(id=id).first()