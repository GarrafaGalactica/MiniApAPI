from flask import jsonify, Blueprint, request, abort
#from app.db import connection
import json
from models.fabricante import Fabricante
from flask_cors import CORS, cross_origin

crearf_api = Blueprint("crearf", __name__, url_prefix="/crearf")


@crearf_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        id = Fabricante.crear(request.form['nombre'],request.form['cod'])
        result = {"Fabricante": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Fabricante": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

listarf_api = Blueprint("listarf", __name__, url_prefix="/listarf")


@listarf_api.get("/")
@cross_origin()
def index():
    lista = Fabricante.listar()
    aux =[]
    if lista:
        print(type(lista[0]))
        i = 0;
        while i < len(lista):
            print(type(lista[i]))
            variable = lista[i]
            aux.append({"Nombre": variable.nombre,"Codigo": variable.codigo})
            i = i + 1
    x = {
        "fabricantes": [
            aux
        ]
        }
    return jsonify(x)

@listarf_api.get("/<int:id>/")
def individual(id):
    fabricante = Fabricante.buscarFabricante(id)
    if fabricante:
        return jsonify({"Id": fabricante.id, "Nombre": fabricante.nombre, "Codigo": fabricante.codigo})
    else:
        abort(404)
    
borrarf_api = Blueprint("borrarf", __name__, url_prefix="/borrarf")

@borrarf_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    print(request.method)
    if request.method == 'POST':
        Fabricante.borrarTodo()
        result = {"Fabricante": "todo borrado"}
        codigo = 200
        return jsonify(result), codigo
    result = {"Fabricante": "es post no get para borrar"}
    codigo = 404
    return jsonify(result), codigo

