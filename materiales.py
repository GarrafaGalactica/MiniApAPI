from flask import jsonify, Blueprint, request, abort
#from app.db import connection
import json
from models.material import Material
from flask_cors import CORS, cross_origin

materiales_api = Blueprint("materiales", __name__, url_prefix="/materiales")


@materiales_api.get("/")
@cross_origin()
def index():
    lista = Material.buscar("",0)
    aux =[]
    i = 0;
    if lista:
        while i < len(lista):
            print(type(lista[i]))
            variable = lista[i]
            aux.append({"Nombre": variable.nombre,"Costo": variable.costo,"Cantidad": variable.cantidad,"Empresa": variable.empresa,"Id": variable.id})
            i = i + 1
    x = {
        "materiales": [
            aux
        ]
        }
    return jsonify(x)