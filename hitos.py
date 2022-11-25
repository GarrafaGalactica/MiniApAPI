from flask import jsonify, Blueprint, request, abort
#from app.db import connection
import json
from models.hitoMateriales import HitoMateriales
from models.hitoFabricacion import HitoFabricantes
from flask_cors import CORS, cross_origin

buscarhm_api = Blueprint("buscarhm", __name__, url_prefix="/buscarhm")

@buscarhm_api.route("/",  methods=('GET', 'POST'))
@cross_origin()
def submit():
    hito = HitoMateriales.buscarHitoMateriales(request.form['reserva'])
    if hito:
        result = hito.descripcion
        HitoMateriales.eliminar(hito.id)
        result = {"Descripcion": result}
        codigo = 200
        return jsonify(result), codigo
    else:
        result = {"Descripcion": "No se registra ningun hito"}
        codigo = 404
        return jsonify(result), codigo

buscarhf_api = Blueprint("buscarhf", __name__, url_prefix="/buscarhf")

@buscarhf_api.route("/",methods=('GET', 'POST'))
@cross_origin()
def submit():
    hito = HitoFabricantes.buscarHitoFabricante(request.form['reserva'])
    if hito:
        result = hito.descripcion
        HitoFabricantes.eliminar(hito.id)
        result = {"Descripcion": result}
        codigo = 200
        return jsonify(result), codigo
    else:
        result = {"Descripcion": "No se registra ningun hito"}
        codigo = 404
        return jsonify(result), codigo

hitofe1_api = Blueprint("hitofe1", __name__, url_prefix="/hitofe1")


@hitofe1_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        id = HitoFabricantes.crear("La mitad de la fabricacion a terminado",request.form['reserva'])
        result = {"Hito": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Hito": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

hitofe2_api = Blueprint("hitofe2", __name__, url_prefix="/hitofe2")


@hitofe2_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        id = HitoFabricantes.crear("Se termino la etapa de fabricacion",request.form['reserva'])
        result = {"Hito": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Hito": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

hitofe3_api = Blueprint("hitofe3", __name__, url_prefix="/hitofe3")


@hitofe3_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        id =HitoFabricantes.crear("Entrega terminada",request.form['reserva'])
        result = {"Hito": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Hito": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

hitome1_api = Blueprint("hitome1", __name__, url_prefix="/hitome1")


@hitome1_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        id = HitoMateriales.crear("Se termino de juntar los materiales",request.form['reserva'])
        result = {"Hito": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Hito": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

hitome2_api = Blueprint("hitome2", __name__, url_prefix="/hitome2")


@hitome2_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        id =HitoMateriales.crear("Los materiales fueron empaquetados",request.form['reserva'])
        result = {"Hito": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Hito": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

hitome3_api = Blueprint("hitome3", __name__, url_prefix="/hitome3")


@hitome3_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        id =HitoMateriales.crear("Se termino la etapa",request.form['reserva'])
        result = {"Hito": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Hito": "es post no get"}
    codigo = 404
    return jsonify(result), codigo
