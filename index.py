from os import path, environ, urandom
from flask import Flask, render_template, g, Blueprint, sessions, jsonify, request, abort
#from app.resources import auth
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update
import handler
from flask_sqlalchemy import SQLAlchemy
from oauthlib.oauth2 import WebApplicationClient
from flask_cors import CORS, cross_origin
from materiales import materiales_api
from estados import rcancelar_api, rfinalizar_api, rretrasar_api
from fabricacion import crearf_api, listarf_api
from reservaF import reservarf_api, listarrf_api, cambiarf_api
from hitos import *
import json
import jwt
import db
from config import config
from models.material import Material
from models.reserva import Reserva
from models.usuario import Usuario

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def home():
    return render_template("home.html")

environment="development"
env = environ.get("FLASK_ENV", environment)
app.config.from_object(config[env])

log_api = Blueprint("log", __name__, url_prefix="/log")
key = "123"


@log_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        user = Usuario.buscarPersona(request.form['nombre'])
        if user.contra == request.form['contra']:
            result = jwt.encode({"nombre": request.form['nombre'], "contra": request.form['contra']}, key, algorithm="HS256")
            codigo = 200
        else:
            result = {"errores": "Not authorized"}
            codigo = 401
        #denuncia = type(denuncia)
        return jsonify(result), codigo

reserva_api = Blueprint("reserva", __name__, url_prefix="/reserva")
key = "123"


@reserva_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        options = {"verify_signature": False}
        print(request.form['cookie'])
        print("XXXXXXXXXXXXXXXXXXXXXXX")
        chequeo = jwt.decode(str(request.form['cookie']), key, algorithms="HS256", options=options)
        print("XXXXXXXXXXXXXXXXXXXXXXX")

        user = Usuario.buscarPersona(chequeo['nombre'])
        if user.contra == chequeo['contra']:
            if (int(request.form['cantidad']) <= int(Material.buscarCantidad(request.form['id']))):
                id = Reserva.crear(request.form['cantidad'],request.form['id'], request.form['fecha'])
                Material.restar(request.form['id'], request.form['cantidad'])
                result = id
                codigo = 200
            else:
                result = {"error": "no hay cantidad suficiente"}
                codigo = 400
        else:
            result = {"errores": "Not authorized"}
            codigo = 401
        #denuncia = type(denuncia)
        return jsonify(result), codigo

crearm_api = Blueprint("crearm", __name__, url_prefix="/crearm")

@crearm_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        id = Material.crear(request.form['nombre'],request.form['costo'],request.form['cantidad'],request.form['empresa'])
        result = {"Material": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Material": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

crearu_api = Blueprint("crearu", __name__, url_prefix="/crearu")

@crearu_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        id = Usuario.crear(request.form['nombre'],request.form['contra'])
        result = {"Persona": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Usuario": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

aumentarm_api = Blueprint("aumentarm", __name__, url_prefix="/aumentarm")

@aumentarm_api.route("/", methods=('GET', 'POST'))
@cross_origin()
def submit():
    if request.method == 'POST':
        Material.aumentar(request.form['id'],request.form['cantidad'])
        result = {"Material": "piola"}
        codigo = 201
        return jsonify(result), codigo
    result = {"Material": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

listaru_api = Blueprint("listaru", __name__, url_prefix="/listaru")

@listaru_api.get("/")
@cross_origin()
def index():
    lista = Usuario.listar()
    aux =[]
    print(type(lista[0]))
    i = 0;
    while i < len(lista):
        print(type(lista[i]))
        variable = lista[i]
        aux.append({"Nombre": variable.nombre,"Contra": variable.contra})
        i = i + 1
    x = {
        "usuarios": [
            aux
        ]
        }
    return jsonify(x)

listarr_api = Blueprint("listarr", __name__, url_prefix="/listarr")

@listarr_api.get("/")
@cross_origin()
def index():
    lista = Reserva.listar()
    aux =[]
    print(type(lista[0]))
    i = 0;
    while i < len(lista):
        print(type(lista[i]))
        variable = lista[i]
        aux.append({"id": variable.id,"Costo": variable.costo,"Cantidad": variable.cantidad,"Material": variable.material, "Estado": variable.estado, "Fecha estimada": variable.fecha_estimada})
        i = i + 1
    x = {
        "reservas": [
            aux
        ]
        }
    return jsonify(x)

@listarr_api.get("/<int:id>/")
def individual(id):
    reserva_row = Reserva.buscarReserva(id)
    material = Material.buscarMaterial(reserva_row.material)
    if reserva_row:
        return jsonify({"Id": reserva_row.id, "Material": material.nombre, "Cantidad": reserva_row.cantidad, "Fecha": reserva_row.fecha_estimada})
    else:
        abort(404)

cambiarm_api = Blueprint("cambiarm", __name__, url_prefix="/cambiarm")

@cambiarm_api.route("/<int:id>/",methods=('GET', 'POST'))
def submit(id):
    if request.method == 'POST':
        Reserva.actualizarFecha(id,request.form['fecha'])
        result = {"Reserva": "piola"}
        codigo = 201
        return jsonify(result), codigo
    result = {"Reserva": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

db.init_app(app)

api = Blueprint("api", __name__, url_prefix="/api")
api.register_blueprint(materiales_api)
api.register_blueprint(log_api)
api.register_blueprint(reserva_api)
api.register_blueprint(crearm_api)
api.register_blueprint(crearu_api)
api.register_blueprint(aumentarm_api)
api.register_blueprint(listaru_api)
api.register_blueprint(listarr_api)
api.register_blueprint(rcancelar_api)
api.register_blueprint(rretrasar_api)
api.register_blueprint(rfinalizar_api)
api.register_blueprint(cambiarm_api)
api.register_blueprint(crearf_api)
api.register_blueprint(listarf_api)
api.register_blueprint(reservarf_api)
api.register_blueprint(listarrf_api)
api.register_blueprint(cambiarf_api)

api.register_blueprint(buscarhm_api)
api.register_blueprint(buscarhf_api)

api.register_blueprint(hitofe1_api)
api.register_blueprint(hitofe2_api)
api.register_blueprint(hitofe3_api)

api.register_blueprint(hitome1_api)
api.register_blueprint(hitome2_api)
api.register_blueprint(hitome3_api)


app.register_blueprint(api)

    #app.register_blueprint(api)

    # Handlers
app.register_error_handler(404, handler.not_found_error)
app.register_error_handler(401, handler.unauthorized_error)

if __name__ == '__main__':
    app.run()