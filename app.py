from flask import Flask, jsonify, request
from ControladorRol import crearRol, consultarRoles, agregarPermisoARol
from ControladorUsuarios import crearUsuario, consultarUsuarios
from ControladorOrdenVenta import consultarOrdenes

app = Flask(__name__)

@app.route("/")
def main_():
    """
    Función principal
    """
    return "Funciona :D"

@app.route("/rol", methods=['POST','GET'])
def roles():
    """
    Controlador de roles
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearRol(data,response_object)  
    elif request.method=="GET":
        response_object=consultarRoles(response_object)  
    return jsonify(response_object)

@app.route("/rol/permiso",methods=['POST','GET','DELETE'])
def permisosRoles():
    """
    Manejo de permisos de roles
    """
    response_object = {'tipo': 'OK'}
    if request.method=='POST':
        data=request.get_json()
        response_object=agregarPermisoARol(data,response_object)
    elif request.method=='GET':
        response_object['ans']="Funciona :D"
    elif request.method=='DELETE':
        response_object['ans']="Se borró"
    return jsonify(response_object)

@app.route("/usuario", methods=['POST','GET'])
def usuarios():
    """
    Controlador de usuarios
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearUsuario(data,response_object)  
    elif request.method=="GET":
        response_object=consultarUsuarios(response_object)  
    return jsonify(response_object)
@app.route("/orden",methods=['POST','GET'])
def ordenVenta():
    """
    Controlador de órdenes de venta
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearUsuario(data,response_object)  
    elif request.method=="GET":
        response_object=consultarOrdenes(response_object)  
    return jsonify(response_object)
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
