from flask import Flask, jsonify, request
from ControladorRol import crearRol, consultarRoles

from dao.RolesDao import RolesDao
from dao.models import Rol
app = Flask(__name__)

@app.route("/")
def main_():
    return "Funciona :D"

@app.route("/rol")
def roles():
    response_object = {'tipo': 'OK'}
    dao=RolesDao()
    if request.method=="POST":
        data=request.get_json()
        response_object=crearRol(dao,data,response_object)  
    elif request.method=="GET":
        response_object=consultarRoles(dao,response_object)  
    return jsonify(response_object)
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
