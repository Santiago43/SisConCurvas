from flask import Flask, jsonify, request
from flask_cors import CORS

from ControladorOrdenVenta import consultarOrdenes
from ControladorRol import agregarPermisoARol, consultarRoles, crearRol
from ControladorUsuarios import consultarUsuarios, crearUsuario, login
from ControladorClientes import consultarClientes
from ControladorInventario import consultarProductos
from ControladorCategorias import consultarCategorias
app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

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

@app.route("/login", methods=['POST'])
def loginUsuario():
    """
    Controlador de login
    """
    response_object = {'tipo': 'OK'}
    data=request.get_json()
    response_object=login(data,response_object)  
    return jsonify(response_object)

@app.route("/cliente",methods=['POST','GET'])
def cliente():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        pass
    else:
        response_object=consultarClientes(response_object)
    return jsonify(response_object)

@app.route("/producto",methods=['POST','GET'])
def producto():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        pass
    else:
        response_object=consultarProductos(response_object)
    return jsonify(response_object)

@app.route("/categoria",methods=['POST','GET'])
def categoria():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        pass
    else:
        response_object=consultarCategorias(response_object)
    return jsonify(response_object)
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
