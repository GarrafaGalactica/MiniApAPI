from os import path, environ, urandom
from flask import Flask, render_template, g, Blueprint, sessions, jsonify, request
#from app.resources import auth
import handler
from oauthlib.oauth2 import WebApplicationClient
from flask_cors import CORS
from materiales import materiales_api
import json
import jwt

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

log_api = Blueprint("log", __name__, url_prefix="/log")
key = "123"


@log_api.route("/", methods=('GET', 'POST'))
def submit():
    if request.method == 'POST':
        chequeo = request.form['rol']
        if chequeo == "operador":
            result = jwt.encode({"Estatus": "ok"}, key, algorithm="HS256")
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
        if chequeo["Estatus"] == "ok":
            result = {"Piola": "ok"}
            codigo = 200
        else:
            result = {"errores": chequeo}
            codigo = 401
        #denuncia = type(denuncia)
        return jsonify(result), codigo

api = Blueprint("api", __name__, url_prefix="/api")
api.register_blueprint(materiales_api)
api.register_blueprint(log_api)
api.register_blueprint(reserva_api)

app.register_blueprint(api)

    #app.register_blueprint(api)

    # Handlers
app.register_error_handler(404, handler.not_found_error)
app.register_error_handler(401, handler.unauthorized_error)

if __name__ == '__main__':
    app.run()