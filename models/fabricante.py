from typing import List
from unittest import result
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update, and_
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from db import db

class Fabricante(db.Model):
    __tablename__ = "fabricantes"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(100))
    codigo = Column(Integer)

    def __init__(self, nombre=None, codigo=None):
        self.nombre = nombre
        self.codigo = codigo

    def crear(nombre, codigo):
        fabricante= Fabricante(nombre,codigo)
        db.session.add(fabricante)
        db.session.commit()
        return fabricante.id
    
    def listar():
        return Fabricante.query.all()
    
    def buscarFabricante(id):
        return Fabricante.query.filter_by(id=id).first()
    
    def borrarTodo():
        Fabricante.query.delete()
        db.session.commit()