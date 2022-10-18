from os import path, environ, urandom
from flask import Flask, render_template, g, Blueprint, sessions
#from app.resources import auth
import handler
from oauthlib.oauth2 import WebApplicationClient
from flask_cors import CORS
from materiales import materiales_api

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

api = Blueprint("api", __name__, url_prefix="/api")
api.register_blueprint(materiales_api)

app.register_blueprint(api)

    #app.register_blueprint(api)

    # Handlers
app.register_error_handler(404, handler.not_found_error)
app.register_error_handler(401, handler.unauthorized_error)

if __name__ == '__main__':
    app.run()