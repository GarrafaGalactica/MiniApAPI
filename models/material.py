from typing import List
from unittest import result
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from db import db

class Material(db.Model):
    __tablename__ = "materiales"
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
        material= Material(nombre,costo,cantidad,empresa)
        db.session.add(material)
        db.session.commit()
        return material.id

    def buscarCosto(id):
        material = Material.query.filter_by(id=id).first()
        return material.costo
    
    def buscarCantidad(id):
        material = Material.query.filter_by(id=id).first()
        return material.cantidad
    
    def buscar(self,nombre,cantidad):
        return db.select(["*"]).where(db._(self.materiales.columns.nombre == nombre))