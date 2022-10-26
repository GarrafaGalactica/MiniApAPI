from flask import jsonify, Blueprint, request, abort
#from app.db import connection
import json
from models.material import Material

materiales_api = Blueprint("materiales", __name__, url_prefix="/materiales")


@materiales_api.get("/")
def index():
    lista = Material.buscar("",0)
    aux =[]
    print(type(lista[0]))
    i = 0;
    while i < len(lista):
        print(type(lista[i]))
        variable = lista[i]
        aux.append({"Nombre": variable.nombre,"Costo": variable.costo,"Cantidad": variable.cantidad,"Empresa": variable.empresa})
        i = i + 1
    x = {
        "materiales": [
            aux
        ]
        }
    return jsonify(x)