from flask import jsonify, Blueprint, request, abort
#from app.db import connection
import json
import jwt
from flask_cors import CORS, cross_origin

log_api = Blueprint("log", __name__, url_prefix="/log")
key = "asdadadadadad"


@log_api.route("/", methods=('POST'))
@cross_origin()
def submit():
    chequeo = request.form['rol']
    if chequeo["rol"] == "operador":
        result = jwt.encode({"Estatus": "ok"}, key, algorithm="HS256")
        codigo = 201
    else:
        result = {"errores": "Not authorized"}
        codigo = 401
    #denuncia = type(denuncia)
    return jsonify(result), codigo