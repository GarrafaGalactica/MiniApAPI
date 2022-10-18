from flask import jsonify, Blueprint, request, abort
#from app.db import connection
import json

materiales_api = Blueprint("materiales", __name__, url_prefix="/materiales")


@materiales_api.get("/")
def index():
    x = {
        "materiales": [
            {"meterial": "vidrio", "precio": 3000, "cantidad": 20, "empresa": "tito vidrio"},
            {"meterial": "vidrio premium", "precio": 7000, "cantidad": 10, "empresa": "tito vidrio"},
            {"meterial": "plastico", "precio": 1000, "cantidad": 50, "empresa": "plxtico"},
            {"meterial": "plastico vegano", "precio": 5000, "cantidad": 15, "empresa": "vegxanxs"},
            {"meterial": "fierros", "precio": 1000, "cantidad": 20, "empresa": "fierreros"},
            {"meterial": "clavos", "precio": 200, "cantidad": 1, "empresa": "bob construcciones"},
            {"meterial": "tornillos", "precio": 1000, "cantidad": 60, "empresa": "bob construcciones"},
            {"meterial": "vidrio", "precio": 2000, "cantidad": 13, "empresa": "bob construcciones"},
            {"meterial": "vidrio", "precio": 3000, "cantidad": 20, "empresa": "pepe vidrio"},
            {"meterial": "vidrio premium", "precio": 6000, "cantidad": 0, "empresa": "pepe vidrio"},
            {"meterial": "vidrio", "precio": 1000, "cantidad": 10, "empresa": "vidrios amigables"},
            {"meterial": "clavos", "precio": 300, "cantidad": 20, "empresa": "tom construcciones"},
            {"meterial": "vidrio", "precio": 300, "cantidad": 20, "empresa": "me canse"},
        ]
        }
    return jsonify(x)