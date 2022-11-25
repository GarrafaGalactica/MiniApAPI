from typing import List
from unittest import result
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update, and_
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from db import db

class HitoFabricantes(db.Model):
    __tablename__ = "hitosFabricantes"
    id = Column(Integer,primary_key=True)
    reserva = Column(Integer,ForeignKey('reservasFabricacion.id'))
    descripcion = Column(String(100))

    def __init__(self, descripcion=None, reserva=None):
        self.descripcion = descripcion
        self.reserva = reserva

    def crear(descripcion, reserva):
        hito= HitoFabricantes(descripcion,reserva)
        db.session.add(hito)
        db.session.commit()
        return hito.id
    
    def listar():
        return HitoFabricantes.query.all()
    
    def buscarHitoFabricante(reserva):
        return HitoFabricantes.query.filter_by(reserva=reserva).first()
    
    def eliminar(id):
        hito = HitoFabricantes.query.filter_by(id = id).first()
        db.session.delete(hito)
        db.session.commit()