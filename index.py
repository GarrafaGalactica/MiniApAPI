from os import path, environ, urandom
from flask import Flask, render_template, g, Blueprint, sessions, jsonify, request
#from app.resources import auth
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, update
import handler
from flask_sqlalchemy import SQLAlchemy
from oauthlib.oauth2 import WebApplicationClient
from flask_cors import CORS
from materiales import materiales_api
import json
import jwt
import db
from config import config
from models.material import Material
from models.reserva import Reserva
from models.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

environment="development"
env = environ.get("FLASK_ENV", environment)
app.config.from_object(config[env])

log_api = Blueprint("log", __name__, url_prefix="/log")
key = "123"


@log_api.route("/", methods=('GET', 'POST'))
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
def submit():
    if request.method == 'POST':
        chequeo = jwt.decode(request.form['cookie'], key, algorithms="HS256")
        user = Usuario.buscarPersona(chequeo['nombre'])
        if user.contra == chequeo['contra']:
            if (int(request.form['cantidad']) <= int(Material.buscarCantidad(request.form['id']))):
                id = Reserva.crear(request.form['cantidad'],request.form['id'])
                Material.restar(request.form['id'], request.form['cantidad'])
                result = {"reserva_id": id}
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
def submit():
    if request.method == 'POST':
        id = Usuario.crear(request.form['nombre'],request.form['contra'])
        result = {"Persona": id}
        codigo = 201
        return jsonify(result), codigo
    result = {"Usuario": "es post no get"}
    codigo = 404
    return jsonify(result), codigo

db.init_app(app)

api = Blueprint("api", __name__, url_prefix="/api")
api.register_blueprint(materiales_api)
api.register_blueprint(log_api)
api.register_blueprint(reserva_api)
api.register_blueprint(crearm_api)
api.register_blueprint(crearu_api)

app.register_blueprint(api)

    #app.register_blueprint(api)

    # Handlers
app.register_error_handler(404, handler.not_found_error)
app.register_error_handler(401, handler.unauthorized_error)

if __name__ == '__main__':
    app.run()