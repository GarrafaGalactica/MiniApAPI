from flask import jsonify, Blueprint, request, abort
#from app.db import connection
import json
from models.reservaFabricacion import ReservaFabricacion
from flask_cors import CORS, cross_origin

reservarf_api = Blueprint("reservarf", __name__, url_prefix="/reservarf")


@reservarf_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        if ReservaFabricacion.libre(request.form['fecha1'],request.form['fecha2'],request.form['fabricante']):
            id = ReservaFabricacion.crear(request.form['fabricante'],request.form['fecha1'],request.form['fecha2'])
            result = {"ReservaF": id}
            codigo = 201
            return jsonify(result), codigo
        else:
            result = {"Problema": "No se puede reservar para dicho peirodo de tiempo"}
            codigo = 400
            return jsonify(result), codigo
    result = {"ReservaFabricante": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

listarrf_api = Blueprint("listarrf", __name__, url_prefix="/listarrf")


@listarrf_api.get("/")
@cross_origin()
def index():
    lista = ReservaFabricacion.listar()
    aux =[]
    i = 0;
    if lista:
        while i < len(lista):
            print(type(lista[i]))
            variable = lista[i]
            aux.append({"Fabricante": variable.fabricante,"Estado": variable.estado,"Fecha inicial": variable.fecha_inicio, "Fecha final": variable.fecha_final})
            i = i + 1
    x = {
        "Reservas": [
            aux
        ]
        }
    return jsonify(x)

cambiarf_api = Blueprint("cambiarf", __name__, url_prefix="/cambiarf")

@cambiarf_api.route("/<int:id>/",methods=('GET', 'POST'))
def submit(id):
    if request.method == 'POST':
        ReservaFabricacion.actualizarFecha(id,request.form['fecha1'],request.form['fecha2'])
        result = {"Reserva": "piola"}
        codigo = 201
        return jsonify(result), codigo
    result = {"Reserva": "es post no get"}
    codigo = 404
    return jsonify(result), codigo


borrarrf_api = Blueprint("borrarrf", __name__, url_prefix="/borrarrf")

@borrarrf_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    print(request.method)
    if request.method == 'POST':
        ReservaFabricacion.borrarTodo()
        result = {"ReservaFabricante": "todo borrado"}
        codigo = 200
        return jsonify(result), codigo
    result = {"ReservaFabricante": "es post no get para borrar"}
    codigo = 404
    return jsonify(result), codigo