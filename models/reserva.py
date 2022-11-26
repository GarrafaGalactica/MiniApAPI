from typing import List
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from db import db
from models.material import Material
from datetime import date

class Reserva(db.Model):
    tablename = "reservass"
    id = Column(Integer,primary_key=True)
    costo = Column(Integer)
    cantidad = Column(Integer)
    material = Column(Integer,ForeignKey('materiales.id'))
    estado = Column(String(100))
    fecha_estimada = Column(DateTime)
    fecha_entrega = Column(DateTime)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, costo=None, cantidad=None, mID=None, fecha = None):
        self.costo = costo
        self.cantidad = cantidad
        self.material = mID
        self.estado = "iniciado"
        self.fecha_estimada = fecha

    def crear(cantidad, mID, fecha):
        costoT = Material.buscarCosto(mID)
        intCan = int(cantidad)
        costoTe = costoT * intCan
        reserva = Reserva(costoTe,cantidad,mID, fecha)
        db.session.add(reserva)
        db.session.commit()
        return reserva.id

    def listar():
        return Reserva.query.all()
    
    def buscarReserva(id):
        reserva = Reserva.query.filter_by(id=id).first()
        return reserva
    
    def retrasar(id):
        material = Reserva.query.filter_by(id=id).first()
        material.estado = "retrasado"
        db.session.commit()
    
    def finalizar(id):
        reserva = Reserva.query.filter_by(id=id).first()
        reserva.estado = "finalizado"
        reserva.fecha_entrega = date.today()
        db.session.commit()
    
    def cancelar(id):
        material = Reserva.query.filter_by(id=id).first()
        material.estado = "cancelado"
        db.session.commit()
    
    def actualizarFecha(id, fecha):
        reserva = Reserva.query.filter_by(id=id).first()
        reserva.fecha_estimada = fecha
        db.session.commit()
    
    def borrarTodo():
        Reserva.query.delete()
        db.session.commit()
