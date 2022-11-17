from flask import jsonify, Blueprint, request, abort
#from app.db import connection
import json
from models.reserva import Reserva
from flask_cors import CORS, cross_origin

rcancelar_api = Blueprint("rcancelar", __name__, url_prefix="/rcancelar")


@rcancelar_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        Reserva.cancelar(request.form['id'])
        result = {"Reserva": request.form['id']}
        codigo = 201
        return jsonify(result), codigo
    result = {"Reserva": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

rretrasar_api = Blueprint("rretrasar", __name__, url_prefix="/rretrasar")


@rretrasar_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        Reserva.retrasar(request.form['id'])
        result = {"Reserva": request.form['id']}
        codigo = 201
        return jsonify(result), codigo
    result = {"Reserva": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

rfinalizar_api = Blueprint("rfinalizar", __name__, url_prefix="/rfinalizar")


@rfinalizar_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        Reserva.finalizar(request.form['id'])
        result = {"Reserva": request.form['id']}
        codigo = 201
        return jsonify(result), codigo
    result = {"Reserva": "es post no get"}
    codigo = 404
    return jsonify(result), codigo