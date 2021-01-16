from flask import Flask, jsonify, request
from flask_cors import CORS

from ControladorOrdenVenta import consultarOrdenes
from ControladorRol import consultarRoles, crearRol,actualizarRol, eliminarRol, agregarPermisoARol, removerPermisoARol
from ControladorUsuarios import consultarUsuarios, crearUsuario, login, actualizarUsuario, eliminarUsuario
from ControladorClientes import crearCliente, consultarClientes, actualizarCliente, eliminarCliente
from ControladorInventario import crearProducto, consultarProductos, actualizarProducto, eliminarProducto
from ControladorCategorias import crearCategoria, consultarCategorias
app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def main_():
    """
    Función principal
    """
    return "Funciona :D"

@app.route("/rol", methods=['POST','GET'])
def rol():
    """
    Ruta de roles para crear y consultar
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearRol(data,response_object)  
    elif request.method=="GET":
        response_object=consultarRoles(response_object)  
    return jsonify(response_object)

@app.route("/rol/<rol_ID>", methods=['PUT','DELETE'])
def single_rol(rol_ID):
    """
    ruta de roles para actualizar y eliminar
    """
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=actualizarRol(data,response_object,rol_ID)  
    elif request.method=="DELETE":
        response_object=eliminarRol(response_object,rol_ID)  
    return jsonify(response_object)

@app.route("/rol/permiso/<rol_ID>/<permiso_ID>",methods=['POST','DELETE'])
def permisosRol(rol_ID,permiso_ID):
    """
    Manejo de permisos de roles
    """
    response_object = {'tipo': 'OK'}
    if request.method=='POST':
        response_object=agregarPermisoARol(response_object,rol_ID,permiso_ID)
    elif request.method=='GET':
        response_object['ans']="Funciona :D"
    elif request.method=='DELETE':
        response_object=removerPermisoARol(response_object,rol_ID,permiso_ID)
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

@app.route("/usuario/<documento>", methods=['PUT','DELETE'])
def single_usuario(documento):
    """
    Controlador de usuarios
    """
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=actualizarUsuario(data,response_object,documento)  
    elif request.method=="DELETE":
        response_object=eliminarUsuario(response_object,documento)  
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
    """
    Ruta de clientes para crear y consultar
    """
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearCliente(data,response_object)
    else:
        response_object=consultarClientes(response_object)
    return jsonify(response_object)

@app.route("/cliente/<telefono>",methods=['PUT','DELETE'])
def single_cliente(telefono):
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=actualizarCliente(data,response_object,telefono)
    elif request.method=="DELETE":
        response_object=eliminarCliente(response_object,telefono)
    return jsonify(response_object)

@app.route("/producto",methods=['POST','GET'])
def producto():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearProducto(data,response_object)
    else:
        response_object=consultarProductos(response_object)
    return jsonify(response_object)

@app.route("/producto/<referencia>",methods=['PUT','DELETE'])
def single_producto(referencia):
    response_object = {'tipo': 'OK'}
    if request.method=="PUT":
        data=request.get_json()
        response_object=actualizarProducto(data,response_object,referencia)
    elif request.method=="DELETE":
        response_object=eliminarProducto(response_object,referencia)
    return jsonify(response_object)

@app.route("/categoria",methods=['POST','GET'])
def categoria():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearCategoria(data,response_object)  
    else:
        response_object=consultarCategorias(response_object)
    return jsonify(response_object)

@app.route("/empaque",methods=['POST','GET'])
def empaque():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        response_object=crearCategoria(data,response_object)  
    else:
        response_object=consultarCategorias(response_object)
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
