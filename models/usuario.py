from typing import List
from unittest import result
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update, and_
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from db import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(100))
    contra = Column(String(100))

    def __init__(self, nombre=None, contra=None):
        self.nombre = nombre
        self.contra = contra

    def crear(nombre, contra):
        user= Usuario(nombre,contra)
        db.session.add(user)
        db.session.commit()
        return user.id

    def buscarPersona(nombre):
        user = Usuario.query.filter_by(nombre=nombre).first()
        return user
    
    def listar():
        return Usuario.query.all()