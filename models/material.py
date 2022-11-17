from typing import List
from unittest import result
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update, and_
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
    
    def aumentar(id,x):
        material = Material.query.filter_by(id=id).first()
        material.cantidad = material.cantidad + int(x)
        db.session.commit()
    
    def restar(id,x):
        material = Material.query.filter_by(id=id).first()
        material.cantidad = material.cantidad - int(x)
        db.session.commit()

    def buscarCosto(id):
        material = Material.query.filter_by(id=id).first()
        return material.costo
    
    def buscarCantidad(id):
        material = Material.query.filter_by(id=id).first()
        return material.cantidad
    
    def buscarMaterial(id):
        return Material.query.filter_by(id=id).first()

    def buscar(nombre,cantidad):
        #return db.select(["*"]).where(db.and_(self.materiales.columns.nombre == nombre,self.materiales.columns.cantidad <= cantidad))
        if nombre == "":
            material = Material.query.filter(Material.cantidad >= cantidad)
        else:
            material = Material.query.filter(and_(Material.nombre == nombre,Material.cantidad <= cantidad))
        print(material.all())
        print(material.all())
        print(material.all())
        print(material.all())
        return material.all()