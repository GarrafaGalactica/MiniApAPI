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

    def __init__(self, fabricante=None, fechaI=None, fechaF=None):
        self.fabricante = fabricante
        self.fecha_inicio = fechaI
        self.fecha_final = fechaF
        self.estado = "reservado"

    def crear(fabricante, fechaI, fechaF):
        reserva= ReservaFabricacion(fabricante,fechaI, fechaF)
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
    
    def libre(f1, f2, fabricante):
        libre = True
        if ReservaFabricacion.query.filter(db.and_(ReservaFabricacion.fecha_inicio <= f1, ReservaFabricacion.fecha_final >= f1, ReservaFabricacion.fabricante == fabricante)).first():
            print(1)
            libre = False
        if ReservaFabricacion.query.filter(db.and_(ReservaFabricacion.fecha_inicio <= f2, ReservaFabricacion.fecha_final >= f2, ReservaFabricacion.fabricante == fabricante)).first():
            print(2)
            libre = False
        if ReservaFabricacion.query.filter(db.and_(ReservaFabricacion.fecha_inicio >= f1, ReservaFabricacion.fecha_final <= f2, ReservaFabricacion.fabricante == fabricante)).first():
            print(3)
            libre = False
        return libre
    
    def actualizarFecha(id, f1,f2):
        reserva = ReservaFabricacion.query.filter_by(id=id).first()
        reserva.fecha_inicio = f1
        reserva.fecha_final = f2
        db.session.commit()